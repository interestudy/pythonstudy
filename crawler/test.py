# _*_ coding:utf-8 _*_
# @Author    :ran
# @time      :2018-12-01 18:32
# @File      :ta.py
# @Software  :PyCharm
import re
import socket
from urllib import error
from urllib import request
from urllib.request import urlopen

from bs4 import BeautifulSoup


def open_website_url(website_url):
    with urlopen(website_url) as r:
        date = r.read().decode('gbk')
        # 正则表达式匹配所有的链接
        # res = re.findall(r'href="(.*?)"', date)
        return date


def download_picture(date):
    soup = BeautifulSoup(date, "html.parser")
    pic_ul = soup.find('ul', {"class": "st-list cfix"})
    pic_li = pic_ul.find_all('li')
    for d in pic_li:
        pic_url = d.find('img')['src']
        pic_name = d.find_all('a')[2].attrs['title']
        pic_name = re.sub('[\/:*?"<>|]', '-', pic_name)
        # 创建保存路径
        pic_path = '/users/ran/study/pythonCrawler/xiezhen/'
        # os.makedirs(pic_path)
        try:
            socket.setdefaulttimeout(30)
            request.urlretrieve(pic_url, pic_path + pic_name + '.jpg')
        except error.HTTPError as err:
            print(err)
        print(pic_name + "~~~~~~~~~~~~~~~~~~保存成功")


def do_it(i, website_url):
    while i < 60:
        website_url_nex = website_url + 'index{}.html'.format(i)
        print(website_url)
        print(website_url_nex)
        download_picture(open_website_url(website_url_nex))
        i = i + 1
        website_url_nex = website_url

# req = request.Request('url')
# req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64)
# AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1')
# request.urlopen(req)
# with request.urlopen(req) as f:
#     # print('Status:', f.status, f.reason)
#     # for k, v in f.getheaders():
#     #     print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('gbk'))


def print_data(internal_data):
    print(internal_data)


if __name__ == "__main__":
    do_it(2, "url")
    data = [4, 5, 6]
    print_data(data)

