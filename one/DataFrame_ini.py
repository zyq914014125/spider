import glob
import csv
import re
import plotly.plotly as py
import plotly.graph_objs as go
py.plotly.tools.set_credentials_file(username='justhavefun', api_key='CJ3MefmMgV6T1EDowJ5O')#登陆plotly
class make_plot(object):
    def __init__(self):
        self.salary_min=[]
        self.salary_max=[]
        self.company=[]
        self.w_s=[]
#CSV表合并，暂时无用
    # def csv_merge(self):
    #     csvx_list = glob.glob('*.csv')
    #     for i in csvx_list:
    #         fr = open(i, 'r').read()
    #         with open('all.csv', 'a') as f:
    #             f.write(fr)
#对薪资处理
    def one_job_plot(self,name):
        with open(name, 'r',encoding="utf-8") as f:
            reader = csv.DictReader(f)
            self.company = [row['company'] for row in reader]
        with open(name, 'r', encoding="utf-8") as L:
            res= csv.DictReader(L)
            salary=[row['salary'] for row in res]
            for sa in salary[1:]:
                if len(sa)>1:
                    salary_all= re.findall(r"\d+\.?\d*", sa)
                    chinese=re.findall(r"[\u4e00-\u9fa5]+", sa)
                    if chinese[0]=='千':
                        self.salary_min.append(float(salary_all[0])/10)
                        self.salary_max.append(float(salary_all[1])/10)
                    elif chinese[1]=='年':
                        self.salary_min.append(float(salary_all[0])/12)
                        self.salary_max.append(float(salary_all[1])/12)
                    elif len(salary_all)<2:
                        self.salary_min.append(0)
                        self.salary_max.append(0)
                    else:
                        self.salary_min.append(float(salary_all[0]))
                        self.salary_max.append(float(salary_all[1]))
#绘图
    def make_Barchat(self,na):
            trace1 = go.Bar(
                x=self.company[1:],
                y=self.salary_min,
                name='min/万'
            )
            trace2 = go.Bar(
                x=self.company[1:],
                y=self.salary_max,
                name='max/万'
            )
            data = [trace1, trace2]
            layout=go.Layout(
                    xaxis=dict(tickangle=-45),
                    barmode='group',
                )
            fig = go.Figure(data=data, layout=layout)
            py.plot(fig, filename=na)
    # def make_cityBar(self,na):
    #     trace1 = go.Bar(
    #         x=self.company[1:],
    #         y=self.salary_min,
    #         name='min/万'
    #     )
    #     trace2 = go.Bar(
    #         x=self.company[1:],
    #         y=self.salary_max,
    #         name='max/万'
    #     )
    #     data = [trace1, trace2]
    #     layout = go.Layout(
    #         xaxis=dict(tickangle=-45),
    #         barmode='group',
    #     )
    #     fig = go.Figure(data=data, layout=layout)
    #     py.plot(fig, filename=na)