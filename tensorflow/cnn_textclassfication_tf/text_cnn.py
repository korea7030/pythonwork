import tensorflow as tf
import numpy as np

class TextCNN(object):
    """
    text 분류를 위한 CNN
    embedding layer, convolutional, max-pooling and softmax layer
    """

    def __init__(self, sequence_length, num_classes, vocab_size, embedding_size, filter_sizes, num_filters, l2_reg_lambda=0.0):
        """
        :param sequence_length:문장의 길이(padding 한 문장)
        :param num_classes: 출력층의 class 수(긍정/부정)
        :param vocab_size: 단어집의 수, 임베딩 층의 크기를 정의하기 위해 필요
        :param embedding_size: 임베딩의 차원
        :param filter_sizes: 합성곱 필터가 책임지길 원하는 단어의수
        :param num_filters: 필터 사이즈별 필터의 수
        """

        # placeholder input, output, dropout
        self.input_x = tf.placeholder(tf.int32, [None, sequence_length], name="input_x")
        self.input_y = tf.placeholder(tf.float32, [None, num_classes], name="input_y") # input에 대한 긍정,부정
        self.dropout_keep_prob = tf.placeholder(tf.float32, name="dropout_keep_prob") # dropout 층에서 뉴런을 유지할 확률에 대해서 사용

        # keeping track of L2 regularization loss(optional)
        l2_loss = tf.constant(0.0)

        # Embedding layer
        # 단어집의 단어 인덱스를 저차원 벡터 표현으로 바꿈
        # embedding 시 cpu 강제 실행
        with tf.device('/cpu:0'), tf.name_scope("embedding"):
            self.W = tf.Variable(tf.random_uniform([vocab_size, embedding_size], -1.0, 1.0), name="W")
            self.embedded_chars = tf.nn.embedding_lookup(self.W, self.input_x)
            self.embedded_chars_expanded = tf.expand_dims(self.embedded_chars, -1)

        # filter 크기마다 convolution + maxpool layer 생성
        pooled_outputs = []
        for i, filter_size in enumerate(filter_sizes):
            with tf.name_scope("conv-maxpool-%s" % filter_size):
                # Convolution layer
                filter_shape = [filter_size, embedding_size, 1, num_filters]
                W = tf.Variable(tf.truncated_normal(filter_shape, stddev=0.1), name="W")
                b = tf.Variable(tf.constant(0.1, shape=[num_filters]), name="b")

                conv = tf.nn.conv2d(
                    self.embedded_chars_expanded,
                    W,
                    strides = [1,1,1,1],
                    padding = "VALID",
                    name="conv"
                )

                # Apply nonlinearity
                h = tf.nn.relu(tf.nn.bias_add(conv, b), name="relu")
                # Maxpooling over the outputs
                pooled = tf.nn.max_pool(
                    h,
                    ksize=[1, sequence_length - filter_size + 1, 1,1],
                    strides = [1,1,1,1],
                    padding = 'VALID',
                    name="pool"
                )
                pooled_outputs.append(pooled)

        # pool된 feature를 합침
        num_filters_total = num_filters * len(filter_sizes)
        self.h_pool = tf.concat(3,pooled_outputs)
        self.h_pool_flat = tf.reshape(self.h_pool, [-1,num_filters_total])

        # dropout 추가(학습 시 0.5, 평가시 1(disable dropout))
        with tf.name_scope("dropout"):
            self.h_drop = tf.nn.dropout(self.h_pool_flat, self.dropout_keep_prob)

        # Final
        with tf.name_scope("output"):
            W = tf.get_variable(
                "W",
                shape=[num_filters_total, num_classes],
                initializer = tf.contrib.layers.xavier_initializer())
            b = tf.Variable(tf.constant(0.1, shape=[num_classes]), name="b")
            l2_loss += tf.nn.l2_loss(W)
            l2_loss += tf.nn.l2_loss(b)
            self.scores = tf.nn.xw_plus_b(self.h_drop, W, b, name="scores") # Wx+b 행렬곱을 수행하는 편리한 wrapper 함수
            self.predictions = tf.argmax(self.scores, 1, name="predictions")

        # cross-entropy 손실 평균계산
        with tf.name_scope("loss"):
            # tf.nn.softmax_cross_entropy_with_logits : 정답인 입력 label과 점수가 주어졌을 때, 각 클래스에 대해 cross-entropy를 계산해주는 함수
            losses = tf.nn.softmax_cross_entropy_with_logits(logits=self.scores, labels= self.input_y)
            self.loss = tf.reduce_mean(losses) + l2_reg_lambda * l2_loss

        # Accuracy
        with tf.name_scope("accuracy"):
            correct_predictions = tf.equal(self.predictions, tf.argmax(self.input_y,1))
            self.accuracy = tf.reduce_mean(tf.cast(correct_predictions, "float"), name="accuracy")

