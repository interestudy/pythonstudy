# _*_ coding:utf-8 _*_
# @Author    :ran
# @time      :2018-12-14 15:41
# @File      :mnist_backward.py
# @Software  :PyCharm

"""
反向传播：

"""

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from fully_connected import mnist_forward
import os

BATCH_SIZE = 200
REGULARIZER = 0.0001
LEARNING_RATE_BASE = 0.1
LEARNING_RATE_DECAY = 0.99
MOVING_AVERAGE_DECAY = 0.99
STEPS = 50000
MODEL_SAVE_PATH = "./model/"
MODEL_NAME = "mnist_model"


def backward(mnist):
    # 1.定义占位符
    x = tf.placeholder(tf.float32, [None, mnist_forward.INPUT_NODE])
    y_ = tf.placeholder(tf.float32, [None, mnist_forward.OUTPUT_NODE])
    #  定义训练轮数的变量 定义为不可训练
    global_step = tf.Variable(0, trainable=False)

    # 2.通过前向传播获取预测值
    y = mnist_forward.forward(x, REGULARIZER)

    # 3.用交叉熵方式获取损失函数
    ce = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.arg_max(y_, 1))
    cem = tf.reduce_mean(ce)
    # 最终损失函数loss = cem + losses
    loss = cem + tf.add_n(tf.get_collection('losses'))

    # 4.指数衰减学习率 学习率跟随训练轮数变化动态更新
    learning_rate = tf.train.exponential_decay(
        LEARNING_RATE_BASE,  # 学习率初值
        global_step,  # 当前训练轮数
        mnist.train.num_examples / BATCH_SIZE,
        LEARNING_RATE_DECAY,  # 学习率衰减率
        # staircase 为 true时 global_step / LERANING RATE STEP 取整数 呈阶梯型衰减
        # staircase 为 fase时 学习率是一条平滑下降的曲线
        staircase=True)

    # 5.使用梯度下降的方式训练神经网络
    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=global_step)
    # 定义滑动平均类ema 衰减率为MOVING_AVERAGE_DECAY 衰减率的变量global_step
    ema = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
    # 定义滑动平均的更新列表
    #  tf.trainable_variables() 一个变量用于计算滑动平均，变量的初始值为0，变量的类型必须是实数
    ema_op = ema.apply(tf.trainable_variables())
    with tf.control_dependencies([train_step, ema_op]):
        train_op = tf.no_op(name='train')

    saver = tf.train.Saver()

    # 6.训练会话
    with tf.Session() as sess:
        # 定义并初始化变量
        init_op = tf.global_variables_initializer()
        sess.run(init_op)

        # 添加断点续训功能
        ckpt = tf.train.get_checkpoint_state(MODEL_SAVE_PATH)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)

        for i in range(STEPS):
            xs, ys = mnist.train.next_batch(BATCH_SIZE)
            _, loss_value, step = sess.run([train_op, loss, global_step], feed_dict={x: xs, y_: ys})
            if i % 1000 == 0:
                # print("After %d training step(s), loss on training batch is %g." % (step, loss_value))
                print('After {} training step(s), loss on training batch is {}'.format(step, loss_value))
                # 保存训练后的模型
                saver.save(sess, os.path.join(MODEL_SAVE_PATH, MODEL_NAME), global_step=global_step)


def mian():
    mnist = input_data.read_data_sets("./data/", one_hot=True)
    backward(mnist)


if __name__ == '__main__':
    mian()





