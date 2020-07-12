# _*_ coding:utf-8 _*_
# @Author    :ran
# @time      :2018-12-27 06:41
# @File      :get_bili_emails.py
# @Software  :PyCharm
import csv
import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
'''
曾在B站上传视频，好多人留下邮箱要曲谱，
运行这个小爬虫 把邮箱用csv格式保存下来

1.用selenium 控制浏览器请求，
2.解决页面懒加载的问题
3.beautiful soup来获取页面标签
4.用了一个简单的xpath 条件查找
5.邮箱筛选的正则表达式
6.保存为csv格式的文件
'''


# 启动selenium 不显示浏览器后台静默加载
def get_driver(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # define headless
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # driver = webdriver.Chrome()
    driver.get(url)
    return driver


# 解决页面懒加载 执行通过执行javascript将页面滚动到指定元素
def focus_target(driver):
    time.sleep(5)
    target_elem = driver.find_element_by_xpath("//div[@id='comment']")
    driver.execute_script("arguments[0].scrollIntoView();", target_elem)
    print("已锁定")


def make_csv(emails):  # 保存邮箱到电脑
    with open("/Users/ran/data/bilibili_emails.csv", 'wt',
              newline="", encoding='utf-8') as csv_file:
        write = csv.writer(csv_file)
        write.writerow(emails)


def get_emails(ps, emails):
    for p in ps:    # 遍历列表
        p_text = p.get_text()
        # 用正则表达式匹配并取出评论中的邮箱
        pattern = re.compile('[a-zA-Z0-9*]+@[a-zA-Z0-9]+\.com')
        email = pattern.findall(p_text)
        if email is not None:  # 有些评论没有邮箱 跳过添加到列表
            emails.extend(email)
    return emails


def get_p(driver):  # 获取评论列表
    html = driver.page_source
    soup = BeautifulSoup(html, features="html.parser")
    ps = soup.findAll('p', {'class': 'text'})
    return ps


def next_page(driver, emails):  # 循环下一页 取出所有email
    for i in range(8):
        print('正在执行完第{}页,请稍等......'.format(i))
        time.sleep(5)  # 停止5s等待网络加载
        if i is not 0:  # 跳过首页
            driver.find_element_by_link_text(u'下一页').click()
            time.sleep(5)
        ps = get_p(driver)
        emails = get_emails(ps, emails)
    return emails


def main():
    url = "https://www.bilibili.com/video/av21666145"
    emails = list()

    driver = get_driver(url)
    focus_target(driver)
    emails = next_page(driver, emails)
    make_csv(emails)
    driver.close()


if __name__ == '__main__':
    main()

