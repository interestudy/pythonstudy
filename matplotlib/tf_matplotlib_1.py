# _*_ coding:utf-8 _*_
# @Author    :ran
# @time      :2018-12-11 21:48
# @File      :tf_matplotlib_1.py
# @Software  :PyCharm

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 10)
y = 2*x + 1
y_ = x**2

plt.figure()
plt.plot(x, y)
plt.plot(x, y_)
plt.show()

