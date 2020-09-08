import requests
from lxml import etree
import json
import datetime
import pymysql
import time

def one():
    #第一步下载网页源码
    url="https://ncov.dxy.cn/ncovh5/view/pneumonia?from=timeline&isappinstalled=0"
    #模拟浏览器访问这个网站
    rs = requests.get(url)
    #设置中文字符编码
    rs.encoding ="utf-8"
    #获取网页源码
    html = rs.text
    # print(html);
    #第二步解析源码
    html = etree.HTML(html)
    #第三步提取数据
    info = html.xpath("//script[@id='getAreaStat']/text()")
    #字符串转换
    info = str(info)
    messsage = info[29:-13]
    lists = json.loads(messsage)
    #创建一个省份的空列
    listPName=[]
    #创建一个地区的空列表
    listCity=[]
    nowTime = datetime.datetime.now().strftime("%Y-%m-%d")
    for x in lists:
        #构建元祖数据格式
        t = (nowTime,x["provinceShortName"],None,x["confirmedCount"],x["curedCount"],x["deadCount"])
        #添加省份列表
        listPName.append(t)
        #判断city对应列表是否有数据
        if len(x["cities"])>0:
            for y in x["cities"]:
                tt = (nowTime,x["provinceShortName"],y["cityName"],y["confirmedCount"],y["curedCount"],y["deadCount"])
                listCity.append(tt)


    #查询今日数据是否存在
    iss = select()
    if iss == True:
        print("今日数据已经爬取完毕")
    else:

        two(listPName)

        two(listCity)

#查询
def select():
    #创建数据库连接
   con =  pymysql.connect("localhost","root","123456789","mybits",charset="utf8")
    #创建游标对象
   cur = con.cursor()
    #定义sql字符串
   sql = "select * from info where time = NOW();"
   #运行sql
   cur.execute(sql)
   #拿到查询的结果
   rs = cur.fetchall()  # 打印结果

    # 关闭游标的对象
   cur.close()
    # 关闭数据库连接对象
   con.close()
   #判断查询结果是否有数据
   if len(rs)>0:
       return True
   else:
       return False

#批量插入
def two(m):
    # 创建数据库连接
    con = pymysql.connect("localhost", "root", "123456789", "mybits", charset="utf8")
    # 创建游标对象
    cur = con.cursor()
    # 定义sql
    sql = "insert into info (time,provinceName,areaName,confirmCount,curedCount,deadCount) values(%s,%s,%s,%s,%s,%s)"
    try:
        # 运行sql
        cur.executemany(sql, m)
        # 事务提交
        con.commit()
        print("批量插入成功")
    except Exception as e:
        print(e)
        # 事务
        con.rollback()
        print("批量插入失败")
    finally:
        cur.close()
        con.close()


#定义一个定时任务
def timeTask():
    one()
    while True:
        #每隔3秒运行下面语句块
        time.sleep(5)
        timeTask()
if __name__ =="__main__":
    timeTask()()


