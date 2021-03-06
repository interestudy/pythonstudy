# _*_ coding:utf-8 _*_
# @Author    :ran
# @time      :2019-01-09 07:13
# @File      :train.py
# @Software  :PyCharm
# 用mnist数据集 训练神经网络
import numpy as np
from neural.simple_neural_network import neural_network

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
    # 按照输出层制作真实的数据
    targets = np.zeros(output_nodes) + 0.01
    targets[int(all_values[0])] = 0.99

    n.train(inputs, targets)
    print("is training...")

# 保存权重 方便测试使用(训练好的权重是神经网络的核心)
np.save('who.npy', n.who)
np.save('wih.npy', n.wih)

