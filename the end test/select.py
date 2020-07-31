
import requests
import json

import xlwt
from bs4 import BeautifulSoup
import pymysql
class BS4_set(object):
    #初始
    def __init__(self):
        self.URL="https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start="        #网址
        self.URL2="https://movie.douban.com/j/subject_abstract?subject_id="
        self.Movie=[]
        self.Movie2=[]
        self.id = []
    #获取基础内容
    def _html_init_(self,url):
        header = {
             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
         }
        try:
                session = requests.Session()
                req = session.get(url, headers=header)
                soup=BeautifulSoup(req.text,'html.parser')
                data = json.loads(soup.text)
                for i in range(0, 19):
                    self.Movie.append(data['data'][i])
                    self.id.append(data['data'][i]['id'])
        except Exception:
            pass
    def Star(self,number):
        URL=self.URL
        URL=URL+str(number*20)
        self._html_init_(URL)
        for id1 in self.id:
            URL2 = self.URL2 + str(id1)
            self._html_Details(URL2)
        self.Inserst()
        print('finish')
    #获取详细信息
    def _html_Details(self,url):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        }
        try:
            session = requests.Session()
            req = session.get(url, headers=header)
            soup = BeautifulSoup(req.text, 'html.parser')
            data = json.loads(soup.text)
            self.Movie2.append(data['subject'])
        except Exception:
            pass
    def Inserst(self):
        db = pymysql.connect(host='127.0.0.1', port=3306, user='root1', passwd='123456789', db='movie',
                             charset='utf8')
        cursor = db.cursor()
        try:
           for i in range(0,19):
                directors=str(self.Movie[i]['directors'][0])
                title=str(self.Movie[i]['title'])
                rate=str(self.Movie[i]['rate'])
                url=str(self.Movie[i]['url'])
                cover=str(self.Movie[i]['cover'])
                duration=str(self.Movie2[i]['duration'])
                region=str(self.Movie2[i]['region'])
                release_year=str(self.Movie2[i]['release_year'])
                types =str(self.Movie2[i]['types'][0])
                sql_insert = "insert into movie(directiors,title,rate,url,picture,duration,region,release_year,types) values (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                cursor.execute(sql_insert,[directors,title,rate,url,cover,duration,region,release_year,types])
           message = cursor.fetchall()  # 查看所有数据
           fs = cursor.description
           work = xlwt.Workbook(encoding='utf-8')  # 设置文件编码
           sheet = work.add_sheet('movie1', cell_overwrite_ok=True)  # 添表，第二参数用于确认同一个cell单元是否可以重设值
           for field in range(0, len(fs)):
               sheet.write(0, field, fs[field][0])
           row = 1
           col = 0
           for row in range(1, len(message) + 1):
               for col in range(0, len(fs)):
                   sheet.write(row, col, u'%s' % message[row - 1][col])
           db.commit()
           db.close()
        except Exception as e:
            print(e)
if __name__ == '__main__':

    BS4=BS4_set()
   # with open("./ip_proxy.txt", 'a+') as f:
    #    proxy_line=f.readline()
    BS4.Star(0)




