__author__ = 'Kin'
# coding: utf-8
import requests

#利用API获取代理IP
class ProxyIp :
    API_url = "http://qsrdk.daili666api.com/ip/?"
    retry_time = 1
    retry_mod = 1
    # API_url = "http://www.66ip.cn/getzh.php?"
    IP_list = []
    tid = ""
    def __init__(self,tid,retrymod=1):
        self.tid = tid
        self.retry_mod = retrymod
    def GetIP(self,num):
        self.retry_time+=1
        if(self.retry_time==1000):
            self.retry_time=0
        if(self.retry_time%self.retry_mod!=0):
            return self.IP_list

        suffix = "tid="+str(self.tid)
        suffix+="&num="+str(num)
        # suffix = "getzh="+str(self.tid)
        # suffix += "&getnum="+str(num)
        # suffix +="isp=0&anonymoustype=0&start=&ports=&export=&ipaddress=&area=0&proxytype=2&api=https"

        Total_url = self.API_url+suffix
        try:
            res = requests.get(Total_url)
            # print(res.text)
            # temp = res.text.replace('\t','').replace('\n','').replace(' ','').replace('\r','').split('<br>')
            temp = res.text.replace('\r','').split('\n')
            if(len(temp)>=2):
                self.IP_list = temp
            return self.IP_list
        except:
            return self.IP_list

if __name__=="__main__":
    mproxy = ProxyIp("558551496043441",2)
    print(mproxy.GetIP(3))
    print(mproxy.GetIP(3))
    print(mproxy.GetIP(3))
    print(mproxy.GetIP(3))
    print(mproxy.GetIP(3))
    print(mproxy.GetIP(3))