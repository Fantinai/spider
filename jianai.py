#一个简单的爬取小说的"小爬虫"
from urllib import request
from bs4 import BeautifulSoup
import time

#下载函数
def jianai(page):
    #请求地址
    base_url = "https://mingzhu.zbyw.cn/jianai/%d.html"%page
    #创建一个headers
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }
    #请求信息
    req = request.Request(url=base_url,headers=headers)
    #打开网页
    response = request.urlopen(req)
    #读取网页内容,由于要使用bs4,所以页面就没有utf-8编码了
    html = response.read()
    #创建BeartifulSoup对象
    soup = BeautifulSoup(html,"lxml")
    #获取章节信息,并在末尾加一个回车换行
    unit = soup.select('p[id="shellti"]')[0].get_text()+"\n"
    #获取内容信息,并在末尾加两个回车换行
    text = soup.select('div[class="mzcon"] p')[0].get_text()+"\n\n"
    #创建一个txt文本文件,用于存放获取到的内容,因为要把38章的所有内容存入一个文件,所以使用的是"a"模式
    with open("简爱.txt","a",encoding="utf-8") as file:
        #写入章节
        file.write(unit)
        #写入内容
        file.write(text)
    #华丽的分割线
    print("---------------%d-----------"%page)

if __name__=="__main__":
    #找了一个比较简单的网站,因为只有38章,所以就直接循环了38次
    for page in range(1,39):
        #每次睡3秒
        time.sleep(3)
        jianai(page)


