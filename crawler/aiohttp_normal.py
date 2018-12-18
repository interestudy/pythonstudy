# _*_ coding:utf-8 _*_
# @Author    :ran
# @time      :2018-12-03 10:45
# @File      :aiohttp_normal.py
# @Software  :PyCharm

import requests
import time

URL = 'https://morvanzhou.github.io/'


def normal():
    for i in range(2):
        r = requests.get(URL)
        url = r.url
        print(url)


t1 = time.time()
normal()
print("Normal total time:", time.time()-t1)


'''
https://morvanzhou.github.io/
https://morvanzhou.github.io/
Normal total time: 2.2762057781219482
'''
