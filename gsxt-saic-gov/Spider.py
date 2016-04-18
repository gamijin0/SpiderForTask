# coding: utf-8
import requests
import time
from bs4 import BeautifulSoup as BS
class Spier:
    url = ""
    def __init__(self,url):
        self.url = url

    #获取列表页面
    def GetPage(self,pageNum):
        data  ={
            'condition.pageNo':'6'
        }
        html = requests.post(url=self.url,data = data,verify=False)
        return html.text

    #获取每个页面上的链接信息
    def GetTotalInfo(self,pageNum):
        html = self.GetPage(pageNum)
        bs = BS(html,"html.parser")
        link_list = bs.find_all('a',{"target":"_blank"})
        links = list()
        for i in link_list:
            links.append(i['href'])
        return links

    #获取每条链接的详细信息
    def GetDetailInfo(self,pageNum):

        links = self.GetTotalInfo(pageNum)
        print(links)
        for l in links:
            html = requests.get(l,verify=False)
            print(html)

if __name__=="__main__":
    s= Spier("https://www.sgs.gov.cn/notice/search/ent_except_list")
    s.GetDetailInfo(1)

