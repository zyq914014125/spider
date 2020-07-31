import Se_set
import requests
import json
import xlrd
import xlwt
from bs4 import BeautifulSoup
import pymysql

class BS_4(object):
    def __int__(self):
        self.URL = "https://www.88ys.com/vod-type-id-1-pg-1.html"
        self.movie_name=[]
        self.xpath='//*[@id="wd"]'
        self.movie_url=[]
# #资源网页获取
#     def _html_init_(self, url):
#         header = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
#         }
#         try:
#             session = requests.Session()
#             req = session.get(url, headers=header)
#             soup = BeautifulSoup(req.text, 'html.parser')
#             # 待完成
#         except Exception:
#             pass

# 数据库电影名提出
    def getUrl(self):
        file_name = 'movie.xls'
        file = xlrd.open_workbook(file_name)
        sheet = file.sheet_by_name('movie1')
        row = sheet.nrows
        for i in range(1, row):
            url = sheet.cell_value(i, 2)
            self.movie_name.append(url)
# Se运行
    def Selenium_star(self):
        for i in self.movie_name:
            url=Se_set.browser_input(self.URL,i,self.xpath)
            self.movie_name.append(url)
        Se_set.browser_quiet()
if __name__ == '__main__':
    BS4 = BS_4()
    BS4.getUrl()
    BS4.Selenium_star()