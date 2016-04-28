__author__ = 'RealmL'
# coding: utf-8

import csv
import sys
import os
import requests
from bs4 import BeautifulSoup
from zhuanli import Get_pages
from zhuanli2 import Get_content
from ProxyIP import ProxyIp

class Run_it(object):
    page = Get_pages()
    co = Get_content()
    MyProxy = ProxyIp("558551496043441",2)    #指定从此订单号内获取代理ip

    def get_ip(self):  #  抓ip的脚本
        header = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'
        }
        ips = []
        res = requests.get('http://www.xicidaili.com/', headers = header)

    #   print(res.text)

        bs = BeautifulSoup(res.text,"html.parser")
        links = bs.find_all('tr',{'class':'odd'})
        for link in links:
            tds = link.find_all('td')
            td1 = tds[1]
            td2 = tds[2]
            ip = td1.string+':'+td2.string
            ips.append(ip)
        return ips


    def write_file(self,name,data):
        file_name = name
        with open(file_name, 'a', errors='ignore', newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerows(data)


    def run(self,startPage,endPage):
        start = startPage*10
        ips = self.MyProxy.GetIP(30) #每次获取100个ip

        while(len(ips)<3):
            ips = self.MyProxy.GetIP(30)

        # print(ips)
        ip = ips[0]
        proxies = {
            'http':ip,
            'https':ip
        }
        i = 1
        while start <endPage*10:
            html = self.page.get_html(start,proxies)
            # print(html)
            data = self.co.get_content(html)
            # print(data)
            if data ==[]:
                while True:
                    proxies = {
                        'http':ips[i],
                        'https':ips[i]
                    }
                    try:
                        html = self.page.get_html(start,proxies)

                        data = self.co.get_content(html)
                        if data != []:
                            print('此ip有效')
                            break
                        else:
                            print('换ip')
                            i += 1
                        if i== len(ips):
                            ips = self.MyProxy.GetIP(30) #  更新ip列表
                            print('更新新的ip列表')
                            i = 0
                        # print('gg思密达')
                        # return
                    except:
                        data = []
                        break

            if(int(start/10)>startPage):
                filename_last = "专利"+str(startPage)+"_"+str(int(start/10)-1)+".csv"
            else:
                filename_last = "专利"+str(startPage)+"_"+str(int(start/10))+".csv"
            filename = "专利"+str(startPage)+"_"+str(int(start/10))+".csv"
            if(filename!=filename_last):
                os.rename(filename_last,filename)
            self.write_file(filename,data)
            print(int(start/10)+1,'页写入文件！')
            start += 10
        print('抓取结束！')
if __name__ == '__main__':
    test_it = Run_it()

    print("参数:")
    print(str(sys.argv[1])+"~"+str(sys.argv[2]))

    startPage = sys.argv[1]
    endPage = sys.argv[2]
    test_it.run(int(startPage),int(endPage))







