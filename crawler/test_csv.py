# _*_ coding:utf-8 _*_
# @Author    :ran
# @time      :2018-12-17 15:47
# @File      :test_csv.py
# @Software  :PyCharm

# 测试csv保存数据的方式 以维基百科为例
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/Comparison_of_text_editors')
bsObj = BeautifulSoup(html, features="html.parser")

table = bsObj.findAll("table", {"class": "wikitable"})[0]
rows = table.findAll('tr')

csvFile = open("/Users/ran/data/editors.csv", 'wt', newline="", encoding='utf-8')
write = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['th', 'td']):
            csvRow.append(cell.get_text())
        write.writerow(csvRow)
finally:
    csvFile.close()




