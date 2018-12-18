# _*_ coding:utf-8 _*_
# @Author    :ran
# @time      :2018-12-07 12:21
# @File      :tf_placeholder.py
# @Software  :PyCharm

import tensorflow as tf

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

output = tf.multiply(input1, input2)

with tf.Session() as sess:
    print(sess.run(output, feed_dict={input1: [5.], input2: [3.]}))


