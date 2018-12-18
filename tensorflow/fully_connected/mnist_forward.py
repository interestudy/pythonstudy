# _*_ coding:utf-8 _*_
# @Author    :ran
# @time      :2018-12-14 15:19
# @File      :mnist_forward.py
# @Software  :PyCharm

"""
前向传播:获取权重 偏置 获取输出值
"""
import tensorflow as tf

INPUT_NODE = 784
OUTPUT_NODE = 10
LAYER1_NODE = 500


# 获取权重
def get_weight(shape, regularizer):
    # 获取正态分布的随机数 去掉大偏离点
    w = tf.Variable(tf.truncated_normal(shape, stddev=0.1))
    if regularizer is not None:
        # 使用正则化: 在获取权重的时候 给w也加上权重 从而抑制模型噪声 减小过拟合
        # 正则化后 本例损失函数变为 loss = cem + losses
        # 前向传播中把losses值存起来 方便反向传播中取出
        tf.add_to_collection("losses", tf.contrib.layers.l2_regularizer(regularizer)(w))
    return w


# 获取偏置
def get_bias(shape):
    b = tf.Variable(tf.zeros(shape))
    return b


# 前向传播
def forward(x, regularizer):
    w1 = get_weight([INPUT_NODE, LAYER1_NODE], regularizer)
    b1 = get_bias([LAYER1_NODE])
    y1 = tf.nn.relu(tf.matmul(x, w1) + b1)

    w2 = get_weight([LAYER1_NODE, OUTPUT_NODE], regularizer)
    b2 = get_bias([OUTPUT_NODE])
    y = tf.matmul(y1, w2) + b2
    return y







