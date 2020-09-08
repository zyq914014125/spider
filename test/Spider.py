#原生
import requests
from bs4 import BeautifulSoup
from lxml import etree
import test
import  re


#单页爬取
def BS(URL):
  response = requests.get(URL)
  response.encoding='utf-8'
  html = response.text
  soup= BeautifulSoup(html,'lxml')
  span_text=soup.find_all("span",attrs={'style':'font-size: 12pt;'})
  st = (str(span_text[1]).split('<span style="font-size: 12pt;">'))[1]
  if(st.find('img')!=-1):
    st = (str(span_text[0]).split('<span style="font-size: 12pt;">'))[1]
    st=st.split("<br/>")
    print(st[1])
    st=st[1]
  print(st)
  example = re.compile(r'(\d+)例')
  people = re.compile(r'(\d+)人')
  time=re.compile(r'(\d+)')
  time=(time.findall(st))[0:2]
  list=example.findall(st)
  if(people.findall(st)==[]):
    people = re.compile(r'(\d+)尚')
  list.append((people.findall(st)))
  list.append(test.time_change(time))
  print(list)
  return list

#url爬取
def get_url():
  response = requests.get(test.URL)
  response.encoding = 'utf-8'
  html = response.text
  soup = BeautifulSoup(html, 'lxml')
  div_text=soup.find_all(class_="contMain fontSt")
  list_a=[]
  i=0
  for span in div_text:
    a=span.find_all('a')
    list_a=a
  for a in list_a:
    a_href=a['href']
    i=i+1
    input("http://wsjkw.sc.gov.cn" + a_href)
    print(a_href)
  print("success")

#入库
def input(URL):
  database="pythontest"
  db=test.Mymysql_connect(database)
  #获取游标
  cursor=db.cursor()
  sql="INSERT INTO test1(diagnosis,overseas,cure,dead,treatment,ob,time) VALUES (%s,%s,%s,%s,%s,%s,%s)"
  cursor.execute(sql,BS(URL))
  db.commit()
  db.close()


#打表
def make_excel():
  sql="SELECT * FROM test1;"
  test.excel_make("pythontest",sql,"test1",'C:\\Users\\Administrator\\Desktop\\info.xls')

if __name__ == '__main__':
  make_excel()


