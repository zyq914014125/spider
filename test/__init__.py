import pymysql
import xlrd
import xlwt

URL="http://wsjkw.sc.gov.cn/scwsjkw/gzbd01/ztwzlmgl.shtml"
header = {
             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
         }
#Mysql_connect
def Mymysql_connect(db_name):
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456789', db=db_name,
                         charset='utf8')
    return db


#数据库打表(db_name:表名，sql:sql语句,file_name:表名，file_path:excel表路径）
def excel_make(db_name,sql,file_name,file_path):
    db=Mymysql_connect(db_name)
    cursor = db.cursor()
    try:
        #sql执行
        cursor.execute(sql)
        #游标指向，sql结果集头
        cursor.scroll(0, mode='absolute')
        #结果集全接受
        message = cursor.fetchall()
        #列出字段所有信息（名，长度，类型……）
        information=cursor.description
        #Excle编码设置
        Excel_file= xlwt.Workbook(encoding='utf-8')
        #添表
        sheet = Excel_file.add_sheet(file_name, cell_overwrite_ok=True)
        #数据入表
        for field in range(0, len(information)):
            sheet.write(0, field, information[field][0])
        row = 1
        col = 0
        for row in range(1, len(message) + 1):
            for col in range(0, len(information)):
                sheet.write(row, col, u'%s' % message[row - 1][col])
        #文件保存
        Excel_file.save(file_path)
        #数据库连接关闭
        db.commit()
        db.close()
        print(file_name+".xls,Make success")
    #异常处理
    except Exception as  e:
        print(e)

#时间格式调整
def time_change(time):
    list=time[0]+"-"+time[1]
    return list

#读表
def getUrl():
    file_name = 'movie.xls'
    file = xlrd.open_workbook(file_name)
    sheet = file.sheet_by_name('movie1')
    row = sheet.nrows
    for i in range(1,row):
        url = sheet.cell_value(i, 4)
        