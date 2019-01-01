# _*_ coding:utf-8 _*_
# @Author    :ran
# @time      :2018-12-27 06:41
# @File      :get_bili_emails.py
# @Software  :PyCharm

from selenium import webdriver
import time
import re
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

# 不显示浏览器后台静默加载
chrome_options = Options()
chrome_options.add_argument("--headless")       # define headless
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://www.bilibili.com/video/av21666145")

# 解决页面懒加载 执行通过执行javascript将页面滚动到指定元素
targetElem = driver.find_element_by_xpath("//div[@id='comment']")
driver.execute_script("arguments[0].scrollIntoView();", targetElem)

emails = list()

# 循环下一页
for i in range(8):
    time.sleep(5)   # 停止5s等待网络加载
    # 跳过第一页
    if i is not 0:
        driver.find_element_by_link_text(u'下一页').click()
        time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, features="html.parser")
    ps = soup.findAll('p', {'class': 'text'})

    # 遍历列表
    for p in ps:
        p_text = p.get_text()
        # 用正则表达式匹配并取出评论中的邮箱
        pattern = re.compile('[a-zA-Z0-9*]+@[a-zA-Z0-9]+\.com')
        email = pattern.findall(p_text)
        if email is not None:  # 有些评论没有邮箱 跳过添加到列表
            emails.extend(email)


print(emails)
driver.close()

