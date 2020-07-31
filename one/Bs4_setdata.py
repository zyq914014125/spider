from urllib import request

import DataFrame_ini
import Selenium_ini_
import pandas as pd
from bs4 import BeautifulSoup

from one import treatment


class Bs4_set(object):
    def __init__(self):
        self.url="https://www.51job.com"          #起始地址
        self.data={}                                  #DateFrame表数据
        self.com_name = []                             #公司名
        self.job = []                                   #工作名
        self.salay = []                                  #薪资
        self.put_time = []                                  #发行日期
        self.city = []                                        #城市
        self.href=[]                                            #详情链接
#循环爬取
    def _html_(self,first,page):
        if first:
            print('输入job')
            line = input()
            URL=se.browser_input(line,"kwdselectid","https://www.51job.com")
            self.url=URL
        else:
            URL=se.browser_page_turning("jump_page",self.url,page,"//*[@id='resultList']/div[55]/div/div/div/span[3]")
        response = request.get(URL)
        html = response.read()
        html = html.decode('gb18030')
        soup = BeautifulSoup(html, 'lxml')
        c_name = soup.find_all(class_='t2')
        for name in c_name[1:]:
            a=name.find('a')
            self.com_name.append(a.string.strip())
        for job_name in soup.find_all(class_='t1')[1:]:
              a = job_name.find('a')
              self.href.append(a['href'])
              self.job.append(a.string.strip())
        for money in soup.find_all(class_='t4')[1:]:
            self.salay.append(money.string)
        for city in soup.find_all(class_='t3')[1:]:
            self.city.append(city.string)
        for time in soup.find_all(class_='t5')[1:]:
            self.put_time.append(time.string)
#建表
    def Data_creat(self):
       self.data = {'job': self.job,
                'company': self.com_name,
                'city': self.city,
                'salary': self.salay,
                'data': self.put_time
                }
       self.df = pd.DataFrame(self.data)
    def make_csv(self,name,nameother):
        self.df.to_csv(name)
        tre.build_treatment(self.href, self.com_name,nameother)
if __name__ == '__main__':
    se= Selenium_ini_
    bs4_da=Bs4_set()
    data_= DataFrame_ini
    data_make_=data_.make_plot()
    tre = treatment
#对象建立
    flag=True
    Continue='N'
    co=0
    while True:
        if flag==False:
            Continue = input('是否继续Y/N:')
        if Continue == 'Y'or flag:
            co+=1
            bs4_da._html_(True, 2)
            df1 = bs4_da.Data_creat()
            bs4_da._html_(False, 2)
            df2 = bs4_da.Data_creat()
            bs4_da.make_csv(str(co)+'.csv','href'+str(co+1)+'.csv')

            flag=False
        else:
            break
    Continue = input('是否绘图Y/N:')
    if Continue == 'Y' :
        Continue= input('表名:')
        data_make_.one_job_plot(Continue)
        data_make_.make_Barchat('Bar')
    Continue=input('需要详情吗？')
    if Continue == 'Y':
        name=input('输入公司名:')
        file_name=input('表名：')
        tre.find_treatment(file_name,name)
