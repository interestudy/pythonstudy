# _*_ coding:utf-8 _*_
# @Author    :ran
# @time      :2019-01-09 07:14
# @File      :test.py
# @Software  :PyCharm
import numpy as np
# from simple_neural_network import train

# 测试神经网络
from simple_neural_network.neural_network import NeuralNetwork

test_data_file = open("mnist_train_100.csv", "r")
test_data_list = test_data_file.readlines()
test_data_file.close()

# 新建一个神经网络 从训练好的神经网络中更新权重
n_ = NeuralNetwork(784, 100, 10, 0.2)
n_.who = np.load('who.npy')
n_.wih = np.load('wih.npy')

scorecard = []

for record in test_data_list:
    all_values = record.split(',')
    correct_label = int(all_values[0])
    print(correct_label, "correct label")

    inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    outputs = n_.query(inputs)

    label = np.argmax(outputs)
    print(label, "network's answer")

    if label == correct_label:
        scorecard.append(1)
    else:
        scorecard.append(0)

scorecard_array = np.asarray(scorecard)
print("performance=", scorecard_array.sum() / scorecard_array.size)
