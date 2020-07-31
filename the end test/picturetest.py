import requests
import xlrd
#coding=utf-8
path='G:\sorce'
pictures = []
def getUrl():
    file_name = 'movie.xls'
    file = xlrd.open_workbook(file_name)
    sheet = file.sheet_by_name('movie1')
    row = sheet.nrows
    for i in range(1,row):
        url = sheet.cell_value(i, 4)
        pictures.append(url)
def getSource():
    i = 1
    for pi in pictures:
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        }
        req = requests.get(pi, headers=header)
        name = str(i)
        file_name = path + '\\' + name+'.jpg'
        f = open(file_name, 'wb')
        f.write(req.content)
        f.close()
        i+=1
    print('finish')
if __name__ == '__main__':
    getUrl()
    getSource()