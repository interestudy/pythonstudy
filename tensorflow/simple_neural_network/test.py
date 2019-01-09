# _*_ coding:utf-8 _*_
# @Author    :ran
# @time      :2019-01-09 07:14
# @File      :test.py
# @Software  :PyCharm
import numpy as np
from simple_neural_network import train

# 测试神经网络
test_data_file = open("mnist_test.csv", "r")
test_data_list = test_data_file.readlines()
test_data_file.close()

scorecard = []

for record in test_data_list:
    all_values = record.split(',')
    correct_label = int(all_values[0])
    print(correct_label, "correct label")
    inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    outputs = train.n.query(inputs)
    label = np.argmax(outputs)
    print(label, "network's answer")

    if label == correct_label:
        scorecard.append(1)
    else:
        scorecard.append(0)

scorecard_array = np.asarray(scorecard)
print("performance=", scorecard_array.sum() / scorecard_array.size)
