# _*_ coding:utf-8 _*_
# @Author    :ran
# @time      :2018-12-09 13:09
# @File      :tf_example.py
# @Software  :PyCharm
import tensorflow as tf
import numpy as np

# 创建数据 当做数据源
# rand()函数生成0~1之间均匀分布的随机数
x_data = np.random.rand(100).astype(np.float32)
y_data = 0.1*x_data + 0.2


# TensorFlow 创建最简单的模型机构  =====================
#  构建一个线性模型
Weights = tf.Variable(tf.random_uniform([1], -0.1, 0.1))
biases = tf.Variable(tf.zeros([1]))

y = Weights*x_data + biases

# 二次代价函数
loss = tf.reduce_mean(tf.square(y - y_data))
# 定义一个梯度下降法来进行训练的优化器
optimizer = tf.train.GradientDescentOptimizer(0.2)
# 最小化loss的二次函数
train = optimizer.minimize(loss)
# =====================================================

# 初始化变量
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for step in range(201):
        sess.run(train)
        if step % 20 == 0:
            print(step, sess.run(Weights), sess.run(biases))
