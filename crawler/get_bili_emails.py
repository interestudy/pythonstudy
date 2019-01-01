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


# 循环下一页
for i in range(8):
    time.sleep(2)
    print(i)
    if i is not 0:
        driver.find_element_by_link_text(u'下一页').click()
        time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, features="html.parser")
    ps = soup.findAll('p', {'class': 'text'})
    # 循环取出列表内容
    for j in range(len(ps)):
        p_text = ps[j].get_text()
        pattern = re.compile('[a-zA-Z0-9*]+@[a-zA-Z]+\.com')
        print(pattern.findall(p_text))

driver.close()

