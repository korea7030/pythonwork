# -*- coding: utf-8 -*-
# 구글의 딥마인드 논문 참고용 DQN
# http://www.nature.com/nature/journal/v518/n7540/full/nature14236.html

import tensorflow as tf
import numpy as np
import random
from collections import deque

class DQN:
    # 학습에 사용할 플레이결과를 얼마나 많이 저장해서 사용할지 정함
    # (플레이결과 = 게임판의 상태 + 취한 액션 + 리워드 + 종료여부)
    REPLAY_MEMORY= 10000
    # 학습시 사용/계산할 상태값(정확히는 replay memory)의 개수를 정함
    BATCH_SIZE = 32
    # 과거의 상태에 대한 가중치를 줄이는 역할
    GAMMA = 0.9
    # 한 번에 볼 총 프레임 수
    # 앞의 상태까지 고려하기 위함
    STATE_LEN = 4

    def __init__(self, session, width, height, n_action):
        self.session = session
        self.n_action = n_action
        self.width = width
        self.height= height
        # 게임 플레이결과를 저장할 메모리
        self.memory = deque()
        # 현재 게임판의 상태
        self.state = None

        # 게임의 상태를 입력받을 변수
        # [게임판의 가로 크기, 게임판의 세로 크기, 게임 상태의 개수(현재+과거+과거..)]
        self.input_X = tf.placeholder(tf.float32, [None, width, height, self.STATE_LEN])
        # 각각의 상태를 만들어낸 액션의 값들(0,1,2...)
        self.input_A = tf.placeholder(tf.int64, [None])
        # 손실값을 계산하는데 사용할 입력값.
        self.input_Y = tf.placeholder(tf.float32, [None])

        self.Q = self._build_network('main')
        self.cost, self.train_op = self._build_op()

        # 학습을 더 잘되게 하기 위해
        # 손실값 계산을 위해 사용하는 타겟(실측값)의 Q_value를 계산하는 네트워크를 따로 만들어서 사용
        self.target_Q = self._build_network('target')
        
    def _build_network(self, name):
        with tf.variable_scope(name):
            model = tf.layers.conv2d(self.input_X, 32, [4,4], padding='same', activation=tf.nn.relu)
            model = tf.layers.conv2d(model, 64, [2,2], padding='same', activation=tf.nn.relu)
            model = tf.contrib.layers.flatten(model)
            model = tf.layers.dense(model, 512, activation=tf.nn.relu)

            Q = tf.layers.dense(model, self.n_action, activation=None)

        return Q

    def _build_op(self):
        # DQN의 손실함수를 구성하는 부분
        one_hot = tf.one_hot(self.input_A, self.n_action, 1.0, 0.0)
        Q_value = tf.reduce_sum(tf.multiply(self.Q, one_hot), axis=1)
        cost = tf.reduce_mean(tf.square(self.input_Y - Q_value))
        train_op = tf.train.AdamOptimizer(1e-6).minimize(cost)

        return cost, train_op

    def update_target_network(self):
        copy_op = []

        main_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope='main')
        target_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope='target')

        # 학습 네트워크의 변수의 값들을 타겟 네트워크로 복사해서 타겟 네트워크의 값들을 최신으로 업데이트
        for main_var, target_var in zip(main_vars, target_vars):
            copy_op.append(target_var.assign(main_var.value()))

        self.session.run(copy_op)

    def get_action(self):
        Q_value = self.session.run(self.Q, feed_dict={self.input_X: [self.state]})

        action = np.argmax(Q_value[0])

        return action

    def init_state(self, state):
        # 현재 게임판의 상태를 초기화.
        state = [state for _ in range(self.STATE_LEN)]
        # axis=2 는 input_X 의 값이 다음처럼 마지막 차원으로 쌓아올린 형태로 만들었기 때문
        # self.input_X = tf.placeholder(tf.float32, [None, width, height, self.STATE_LEN])
        self.state = np.stack(state, axis=2)

    def remember(self, state, action, reward, terminal):
        # 학습데이터로 현재의 상태만이 아닌, 과거의 상태까지 고려하여 계산하도록 하였고,
        # 이 모델에서는 과거 3번 + 현재 = 총 4번의 상태를 계산하도록 함
        # 새로운 상태가 들어왔을 때, 가장 오래된 상태를 제거하고 새로운 상태를 넣음
        next_state = np.reshape(state, (self.width, self.height,1))
        next_state = np.append(self.state[:, :, 1:], next_state, axis=2)

        # 플레이결과, 즉 액션으로 얻어진 상태와 보상 등을 메모리에 저장
        self.memory.append((self.state, next_state, action, reward, terminal))

        # 저장할 플레이결과의 개수를 제한
        if len(self.memory) > self.REPLAY_MEMORY:
            self.memory.popleft()

        self.state = next_state

    def _sample_memory(self):
        sample_memory = random.sample(self.memory, self.BATCH_SIZE)

        state = [memory[0] for memory in sample_memory]
        next_state = [memory[1] for memory in sample_memory]
        action = [memory[2] for memory in sample_memory]
        reward = [memory[3] for memory in sample_memory]
        terminal = [memory[4] for memory in sample_memory]

        return state, next_state, action, reward, terminal

    def train(self):
        # 게임 플레이를 저장한 메모리에서 배치 사이즈만큼을 샘플링하여 가져옴
        state, next_state, action, reward, terminal = self._sample_memory()

        # 학습시 다음 상태를 타겟 네트워크에 넣어 target Q value 를 구함
        target_Q_value = self.session.run(self.target_Q, feed_dict={self.input_X: next_state})

        # DQN의 손실함수에 사용할 핵심적인 값을 계산하는 부분
        Y = []
        for i in range(self.BATCH_SIZE):
            if terminal[i]:
                Y.append(reward[i])
            else:
                Y.append(reward[i] + self.GAMMA * np.max(target_Q_value[i]))

        self.session.run(self.train_op, feed_dict= {self.input_X: state, self.input_A : action, self.input_Y: Y})
