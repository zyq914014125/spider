import requests
import threading
from lxml import etree
# 解析网页，并得到网页中的IP代理
def get_proxy(html):
    selector = etree.HTML(html)
    proxies = []
    for each in selector.xpath("//tr[@class='odd']"):
        ip = each.xpath("./td[2]/text()")[0]
        port = each.xpath("./td[3]/text()")[0]
        # 拼接IP地址，端口号6
        proxy = ip + ":" + port
        proxies.append(proxy)
    test_proxies(proxies)

def thread_write_proxy(proxy):
    with open("./ip_proxy.txt", 'a+') as f:
        f.write(proxy + '\n')
# 验证已得到IP的可用性
def thread_test_proxy(proxy):
    url = "http://www.baidu.com/"
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36",
    }
    try:
        response = requests.get(url, headers=header, proxies={"http": proxy}, timeout=1)
        if response.status_code == 200:
            thread_write_proxy(proxy)
    except Exception:
        pass
# 添加线程模式
def test_proxies(proxies):
    proxies = proxies
    for proxy in proxies:
        test = threading.Thread(target=thread_test_proxy, args=(proxy,))
        test.start()
def get_html(url):
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    }

    response = requests.get(url,headers=header)
    get_proxy(response.text)
if __name__ == "__main__":
    url = "http://www.xicidaili.com/nn/"
    for i in range(1,30):
      get_html(url+str(i))

