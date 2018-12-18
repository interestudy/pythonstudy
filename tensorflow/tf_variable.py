# _*_ coding:utf-8 _*_
# @Author    :ran
# @time      :2018-12-06 20:18
# @File      :tf_variable.py
# @Software  :PyCharm

import tensorflow as tf

state = tf.Variable(0, name='counter')
# 定义常量 one
one = tf.constant(1)
# 定义加法 只是定义 并没有直接计算
new_value = tf.add(state, one)
# 把state更新为new_value
# update state by assigning new_value to it.
update = tf.assign(state, new_value)
# 变量需要初始化 常量不需要
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for _ in range(5):
        sess.run(update)
        print('state=>', sess.run(state))
