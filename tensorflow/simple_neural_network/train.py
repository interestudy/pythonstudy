# _*_ coding:utf-8 _*_
# @Author    :ran
# @time      :2019-01-09 07:13
# @File      :train.py
# @Software  :PyCharm
# 用mnist数据集 训练神经网络
import numpy as np
from simple_neural_network import neural_network

input_nodes = 784
hidden_nodes = 200
output_nodes = 10
learning_rate = 0.05

n = neural_network.NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

training_data_file = open("mnist_train.csv", "r")
training_data_list = training_data_file.readlines()
training_data_file.close()

for record in training_data_list:
    all_values = record.split(',')
    inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01

    targets = np.zeros(output_nodes) + 0.01
    targets[int(all_values[0])] = 0.99

    n.train(inputs, targets)
    print("is training...")

