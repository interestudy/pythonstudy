# _*_ coding:utf-8 _*_
# @Author    :ran
# @time      :2018-12-02 18:32
# @File      :ta.py
# @Software  :PyCharm

# 重构爬虫test
# 优化代码格式 添加异常捕获
import os
import re
from urllib import request
from urllib.error import URLError
from urllib.request import urlopen

from bs4 import BeautifulSoup
from requests import HTTPError

# 输入URL 获取soup对象


def get_soup(url, coding):
    try:
        html = urlopen(url).read().decode(coding)
        soup = BeautifulSoup(html, features="html.parser")
    except HTTPError:
        print("HTTPError")
        return None
    except URLError:
        print("URLError")
    else:
        return soup


# 获取通用标签
def get_tag(soup):
    try:
        tag_ul = soup.find('ul', {"class": "st-list cfix"})
        tag_li = tag_ul.find_all('li')
    except AttributeError as e:
        return None
    else:
        return tag_li


# 判断并创建文件夹
def create_file(internal_file_name):
    img_path = '/users/ran/study/pythonCrawler/{}/'.format(internal_file_name)
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    return img_path


# 下载
def download(tag, img_path):
    for d in tag:
        img_url = d.find('img')['src']
        name = d.find_all('a')[2].attrs['title']
        # 过滤非法URL
        if not re.match(r'^https?:/{2}\w.+$', img_url):
            img_url = 'http://' + img_url
        # 过滤名字中的特殊符号
        name = re.sub('[\/:*?"<>|]', '-', name)
        try:
            request.urlretrieve(img_url, img_path + name +'.jpg')
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)
        else:
            print(name + "~~~~~~~~~~OK")


# 执行
def do_it(internal_website, internal_encoding, internal_file_name):
    soup = get_soup(internal_website, internal_encoding)
    tag_li = get_tag(soup)
    img_path = create_file(internal_file_name)
    print(img_path)
    download(tag_li, img_path)


# 辨别网址
def get_website(internal_website, internal_i, internal_file_name):
    if not internal_i == 1:
        return internal_website + internal_file_name + '/index{}.html'.format(i)
    return internal_website + internal_file_name + '/'


website = 'url'
total_pages_number = 12
file_name = 'name'
encoding = 'gbk'

for i in range(1, total_pages_number):
    print(i)
    website_next = get_website(website, i, file_name)
    print(website_next)
    do_it(website_next, encoding, file_name)



