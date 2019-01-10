# _*_ coding:utf-8 _*_
# @Author    :ran
# @time      :2018-12-02 20:53
# @File      :test_for.py
# @Software  :PyCharm
import numpy as np

# for循环前有语句的含义
# for循环取出的每一个结果 复制给列表
list_0 = [i for i in range(7)]
# print(list_0)


# 测试减号 在set中的应用 加号不可用
unseen = set([i for i in range(10)])
seen = set([i*2 for i in range(10)])
page = set([i*2 for i in range(15)])
# print(unseen)
# print(seen)
# print(page)
# print(page - unseen)
# print(page - unseen)

# 从列表中去数据的格式
x_ = np.random.rand(5, 2)
print(x_)
y_ = [[int(x0 + x1 < 1)] for (x0, x1) in x_]
# y = [[x0] for(x0, x1) in x_]
print(y_)
print("------------------------")

# 真是1 假是0 int函数可以用来判断
print(int(3 < 5))
print(int(False))
print(int(True))

# 将列表转换维2数组并进行转置
node = np.array([1, 2, 3], ndmin=2).T
print(node.shape)

