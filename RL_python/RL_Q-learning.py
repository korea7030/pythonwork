import numpy as np
import gym
import matplotlib.pyplot as plt
from gym.envs.registration import register
import random as pr


def rargmax(vector):
    '''random argmax '''
    m = np.amax(vector)
    # print('m', m)

    indices = np.nonzero(vector == m)[0]
    # print('indices : ', indices)

    return pr.choice(indices)


register(
    id='Frozenlake-v3',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name': '4x4',
                'is_slippery': False
            }
)

env = gym.make('Frozenlake-v3')
# env = gym.make('FrozenLake-v0') # 위의 is_slippery 값이 True인 경우

# Q table 생성(위에서 설정한 4x4)
Q = np.zeros([env.observation_space.n, env.action_space.n])

# 회수 지정
num_episodes = 2000
# discount reward
dis = 0.99
# 결과저장 list
rList = []

for i in range(num_episodes):
    state = env.reset()
    #  print(state)
    rAll = 0
    done = False
    e = 1.0 / ((i // 100) + 1)

    while not done:
        if np.random.rand(1) < e:
            action = env.action_space.sample()
        else:
            action = np.argmax(Q[state, :])

        # 새로운 state, reward를 환경으로부터 받음
        new_state, reward, done, _ = env.step(action)

        # Update Q-Table
        Q[state, action] = reward + dis * np.max(Q[new_state, :])
        rAll += reward
        state = new_state
    rList.append(rAll)

print("Success rate:" + str(sum(rList) / num_episodes))
print("Final Q-Table Values")
print("LEFT DOWN RIGHT UP")
print(Q)
plt.bar(range(len(rList)), rList, color="blue")
plt.show()
