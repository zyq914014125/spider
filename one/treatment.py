import csv

import pandas as pd

from one import Selenium_ini_

se= Selenium_ini_
#建立详情表
def build_treatment(HREF,company_name,file_name):
    data = {'href':HREF,
           'company':company_name
                 }
    df = pd.DataFrame(data)
    df.to_csv(file_name)
# #显示详情
def find_treatment(file_name,name):
    with open(file_name, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['company'] == name:
               se.browser_return_show(row['href'])