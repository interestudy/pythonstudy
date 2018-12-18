# _*_ coding:utf-8 _*_
# @Author    :ran
# @time      :2018-12-03 10:19
# @File      :test_asyncio_1.py
# @Software  :PyCharm

# 非异步执行 执行完一个方法再执行另一个
import time


def job(t):
    print('start job', t)
    time.sleep(t)
    print('Job', t, 'takes ', t, 's')


def main():
    [job(t) for t in range(1, 6)]


t1 = time.time()
main()
print("NO async total time : ", time.time() - t1)
