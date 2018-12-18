# _*_ coding:utf-8 _*_
# @Author    :ran
# @time      :2018-12-10 12:07
# @File      :test_add_layer.py
# @Software  :PyCharm
import tensorflow as tf
import numpy as np

INPUT_NODE = 1
LAYER_NODE = 5
OUTPUT_NODE = 1

# 生成一个shape(5, 1)的二维数组
x_data = np.linspace(-1, 1, 5, tf.float32)[:, np.newaxis]

Weights = tf.Variable(tf.random_normal([1, 8]))
# 测试shape
biases = tf.Variable(tf.zeros([1, 8]))  # 结果是二维数组 [[0. 0. 0. 0. 0. 0. 0. 0.]]
biases_ = tf.Variable(tf.zeros([8]))    # 结果是一维数组 [0. 0. 0. 0. 0. 0. 0. 0.]

xs = tf.placeholder(tf.float32, [None, 1])
Wx = tf.matmul(xs, Weights) + tf.constant([1., 2., 3.])


init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    # print(sess.run(biases))
    # print(x_data)
    # print(sess.run(Weights))

    # You must feed a value for placeholder tensor 'Placeholder'
    # with dtype float and shape [?,1]
    # print(sess.run((tf.matmul(xs, Weights))))
    print(sess.run(Wx, feed_dict={xs: x_data}))

    # print(sess.run(biases))
    # print(sess.run(biases_))
    print(sess.run(tf.matmul(xs, Weights), feed_dict={xs: x_data}))
