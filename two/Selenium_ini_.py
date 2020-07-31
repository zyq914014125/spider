import urllib
from urllib import request

from selenium import webdriver
from bs4 import BeautifulSoup
from time import  sleep
browser = webdriver.Chrome('G:\Program Files\chromedriver.exe')
def browser_find_ticket(go_,to_,URL,date):#查票
    browser.get(URL)
    browser.find_element_by_xpath("//*[@id='fromStationText']").click()
    sleep(3)
    browser.find_element_by_xpath("//*[@id='fromStationText']").send_keys(go_)
    sleep(3)
    browser.find_element_by_xpath("//*[@id='toStationText']").click()
    sleep(3)
    browser.find_element_by_xpath("//*[@id='toStationText']").send_keys(to_)
    sleep(3)
    js = 'document.getElementById("train_date").removeAttribute("readonly");'#将日历必须从日历表选择项，去除
    browser.execute_script(js)
    browser.find_element_by_xpath("//*[@id='train_date']").clear()
    sleep(3)
    browser.find_element_by_xpath("//*[@id='train_date']").send_keys(date)
    sleep(5)
    browser.find_element_by_xpath("//*[@id='search_one']").click()
    sleep(2)
# browser_find_ticket("成都南","重庆北","https://www.12306.cn/index/","2019-4-25")
def browser_quiet():
    browser.quit()
def selenium_set_IP(num):#配置代理IP
    with open('ip_proxy.txt', "r") as f:
        ip = f.readlines()
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument("--proxy-server="+ip[num])
        webdriver.Chrome(chrome_options=chromeOptions)
def login_ini_(URL,name,password):#登录
    browser.get(URL)
    browser.find_element_by_class_name("login-hd-account").click()
    sleep(1)
    browser.find_element_by_xpath("//*[@id='J-userName']").send_keys(name)
    sleep(1)
    browser.find_element_by_xpath("//*[@id='J-password']").send_keys(password)
    sleep(2)
    response = request.urlopen(URL)
    html = response.read()
    html = html.decode('gb18030')
    soup = BeautifulSoup(html, 'lxml')
    img=soup.find_all(class_="imgCode")
    if img.get('src') is not None:
        img_url = img.get('src')
        urllib.request.urlretrieve(img_url, "./output/image/"  + ".jpg")
    sleep(2)
    browser.find_element_by_xpath("//*[@id='J-login']").click()


####
    a_list = m_list.find_all('a')
    img_list = m_list.find_all('img')
    score_list = m_list.find_all('strong')
    movie = {}
    for a in a_list:
        movie['Alink'] = a['herf'].string
        number += 1
        Url = a
        # 详解分析
        de_list = self._html_init_(Url).find_all(class_='info')
        if de_list.find('span', property="v:runtime").string != None:
            movie['time'] = de_list.find('span', property="v:runtime").string
        else:
            time = re.findall(r'<span class="pl">片长:</span>(.*?)<br>')
            movie['time'] = str(time)
        movie['update'] = de_list.find('span', property="v:initialReleaseDate").string
        movie['Directors'] = ''
        directors = de_list.find_all('a', rel="v:directedBy")
        for director in directors:
            movie['Directors'] += director.text
            movie['Directors'] += ''
        movie['Category'] = ''
        categorys = de_list.find_all('span', property="v:genre")
        for category in categorys:
            movie['Category'] += category.text
            movie['Category'] += '  '
        for img in img_list:
            movie['Picture'] = img['src']
        for score in score_list:
            movie['score'] = score.string
        self.Movie.append(movie)