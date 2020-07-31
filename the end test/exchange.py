import requests
import json

import xlwt
from bs4 import BeautifulSoup
import pymysql
def change():
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root1', passwd='123456789', db='movie',
                         charset='utf8')
    cursor = db.cursor()
    try:
        cursor.execute('select * from movie')
        cursor.scroll(0, mode='absolute')
        message = cursor.fetchall()  # 查看所有数据
        fs = cursor.description
        file = xlwt.Workbook(encoding='utf-8')  # 设置文件编码
        sheet = file.add_sheet('movie1', cell_overwrite_ok=True)  # 添表，第二参数用于确认同一个cell单元是否可以重设值
        for field in range(0, len(fs)):
            sheet.write(0, field, fs[field][0])
        row = 1
        col = 0
        for row in range(1, len(message) + 1):
            for col in range(0, len(fs)):
                sheet.write(row, col, u'%s' % message[row - 1][col])
        file.save('C:\\Users\\Administrator\\Desktop\\movie.xls')
        db.commit()
        db.close()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    change()



