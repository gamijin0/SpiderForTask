__author__ = 'Kin'
# coding: utf-8
import requests

#利用API获取代理IP
class ProxyIp :
    # API_url = "http://qsrdk.daili666api.com/ip/?"
    API_url = "http://www.66ip.cn/getzh.php?"
    IP_list = []
    tid = ""
    def __init__(self,tid):
        self.tid = tid
    def GetIP(self,num):
        # getzh=2016040499814
        suffix = "getzh="+str(self.tid)
        suffix += "&getnum="+str(num)
        suffix +="isp=0&anonymoustype=0&start=&ports=&export=&ipaddress=&area=0&proxytype=2&api=https"

        Total_url = self.API_url+suffix
        res = requests.get(Total_url)
        self.IP_list = res.text.replace('\t','').replace('\n','').replace(' ','').replace('\r','').split('<br>')
        return self.IP_list

if __name__=="__main__":
    mproxy = ProxyIp("2016040562884")
    print(mproxy.GetIP(10))