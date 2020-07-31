import collections
from urllib import request
import xlwt
from bs4 import BeautifulSoup
class analysis(object):
    def __init__(self):
        self.head = ['日期', '期号', '', '中奖号第一位', '中奖号第二位', '中奖号第三位']
        self.head2=['日期', '期号', '', '中奖号第一位', '中奖号第二位', '中奖号第三位']
        self.file = xlwt.Workbook(encoding='utf-8')
        self.table = self.file.add_sheet('3D总表', cell_overwrite_ok=True)
        self.table2 = self.file.add_sheet('多位重复表', cell_overwrite_ok=True)
        self.td=[]
        self.first_fire_number = []
        self.second_fire_number = []
        self.third_fire_number = []
    def find_html(self):
        text=''
        for number in range(20):
                URL = 'http://kaijiang.zhcw.com/zhcw/html/3d/list_'+str(number+1)+'.html'
                response = request.urlopen(URL)
                html = response.read()
                html = html.decode("utf-8")
                soup = BeautifulSoup(html, 'lxml')
                tr = soup.find_all('tr')
                for tr_list in tr:
                    td_list = tr_list.find_all('td')
                    ui = []
                    for td in td_list:
                        ui.append(td.string)
                    em_list = tr_list.find_all('em')
                    for em in em_list:
                        ui.append(em.string)
                        del ui[2:4]
                    if len(ui):
                        self.td.append(ui)
    def analysis_number(self):
        for i in self.td[:len(self.td)-1]:
            if   len(i)>1:
                 self.first_fire_number.append(i[3])
                 self.second_fire_number.append(i[4])
                 self.third_fire_number.append(i[5])
    # 打表
    def save_in_excel(self):
        L = 1
        for i in range(0,6):
           self.table.write(0,i,self.head[i])
           self.table2.write(0,i,self.head[i])
        for j in self.td[0:len(self.td)-1]:
            for k in range (0,6):
                if len(j) > 1:
                    self.table.write(L,k,j[k])
            L +=1
    def data_analysis(self):
        count = 0
        count_all=0
        print('一位最火', collections.Counter(self.first_fire_number).most_common(5))
        print('二位最火', collections.Counter(self.second_fire_number).most_common(5))
        print('三位最火', collections.Counter(self.third_fire_number).most_common(5))
        line=0
        for n in self.td[0:len(self.td)-1]:
            now=n
            if len(set(n[-3:])) < 2:
                if len(now) > 1:
                    count+=1
            elif len(set(n[-3:])) < 3:
                if len(now) > 1:
                    line += 1
                    count_all += 1
                    for k in range(6):
                        self.table2.write(line, k, now[k])
            self.file.save('C:\\Users\\Administrator\\Desktop\\test.xls')
        percent = round(count / (len(self.td) - 1), 4)
        percent_all = round(count_all / (len(self.td) - 1), 4)
        print('2位重复率', format(float(percent_all) * 100), '%')
        print('完全位重复率',format(float(percent) * 100),'%')
if __name__ == '__main__':
    analysis=analysis()
    analysis.find_html()
    analysis.analysis_number()
    analysis.save_in_excel()
    analysis.data_analysis()
