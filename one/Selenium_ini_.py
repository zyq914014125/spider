from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import  sleep
browser = webdriver.Chrome('G:\Program Files\chromedriver.exe')
#作为起始页开始输入工作，并通过网页查找
def browser_input(job,element_id,URL):
    browser.get(URL)
    browser.find_element_by_id(element_id).send_keys(job)
    sleep(3)                                                        #等待加载，也可以防止访问过快，卡死服务器
    browser.find_element_by_id(element_id).send_keys(Keys.ENTER)
    sleep(3)
    return format(browser.current_url)
#翻页
def browser_page_turning(element_id,URL,page,element_click):
    browser.get(URL)
    browser.find_element_by_id(element_id).clear()
    browser.find_element_by_id(element_id).send_keys(page)
    sleep(5)
    browser.find_element_by_xpath(element_click).click()     #该网页由span作为模仿按钮，通过class,id都定位不了，所以我才去寻找它的XPATH定位
    sleep(3)
    return format(browser.current_url)
#回显
def browser_return_show(URL):
    browser.get(URL)
def browser_quiet():
    browser.quit()

