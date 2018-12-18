# _*_ coding:utf-8 _*_
# @Author    :ran
# @time      :2018-12-06 19:21
# @File      :tf_session.py
# @Software  :PyCharm
import tensorflow as tf

# create two matrixes
# 矩阵乘的条件是 左列数=右行数
matrix1 = tf.constant([[3, 4],
                       [2, 3]])
matrix2 = tf.constant([[2, 1, 1],
                       [1, 2, 3]])
product = tf.matmul(matrix1, matrix2)

# method 1
# sess = tf.Session()
# result = sess.run(product)
# print(result)
# sess.close()

# method 2
with tf.Session() as sess:
    print(matrix1)
    print(matrix2)
    result = sess.run(product)
    print(sess.run(matrix1))
    print(sess.run(matrix2))
    print(result)


