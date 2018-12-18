# _*_ coding:utf-8 _*_
# @Author    :ran
# @time      :2018-12-10 13:21
# @File      :tf_add_layer.py
# @Software  :PyCharm
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


# 创建神经层
def add_layer(inputs, int_size, out_size, activation_function=None):
    weights = tf.Variable(tf.random.normal([int_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    wx_plus_b = tf.matmul(inputs, weights) + biases
    if activation_function is None:
        outputs = wx_plus_b
    else:
        outputs = activation_function(wx_plus_b)
    return outputs


# 创建数据
x_data = np.linspace(-1, 1, 100)[:, np.newaxis]
noise = np.random.normal(0, 0.1, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise
# 定义占位符
xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])

# 添加隐藏层 和 输出层
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)
prediction = add_layer(l1, 10, 1, activation_function=None)
# 二次代价函數 : loss = mean((y - prediction)^2)
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),
                                    reduction_indices=[1]))
# 定义训练 使用梯度下降法
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
# 定义 变量初始化
init = tf.global_variables_initializer()


# plot the real data
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x_data, y_data)
plt.ion()
plt.show()

# 开始训练
with tf.Session() as sess:
    sess.run(init)
    for step in range(1000):
        sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
        if step % 50 == 0:
            # to visualize the result and improvement
            try:
                ax.lines.remove(lines[0])
            except Exception:
                pass
            prediction_value = sess.run(prediction, feed_dict={xs: x_data})
            # plot the prediction
            lines = ax.plot(x_data, prediction_value, 'r-', lw=2)
            plt.pause(1)








