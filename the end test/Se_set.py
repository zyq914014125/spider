
from selenium import webdriver
from bs4 import BeautifulSoup
from time import  sleep
# 浏览器预载
# //*[@id="wd"]   输入框
# /html/body/div[2]/div[1]/ul[3]/form/input[2] 提交按钮
from selenium.webdriver.common.keys import Keys
#网页搜索
browser = webdriver.Chrome('G:\Program Files\chromedriver.exe')

def browser_input(URL,MovieName,element_id):
    browser.get(URL)
    browser.find_element_by_xpath(element_id).send_keys(MovieName)
    sleep(5)                                                        #网页加载
    browser.find_element_by_xpath(element_id).send_keys(Keys.ENTER)
    sleep(5)
    return format(browser.current_url)
def browser_quiet():
    browser.quit()