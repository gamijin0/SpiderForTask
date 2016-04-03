__author__ = 'Kin'
# coding: utf-8
import requests

#利用API获取代理IP
class ProxyIp :
    API_url = "http://qsrdk.daili666api.com/ip/?"
    IP_list = []
    tid = ""
    def __init__(self,tid):
        self.tid = tid
    def GetIP(self,num,category=2,thefilter="on",sortby="speed"):
        suffix = "tid="+self.tid
        suffix +="&num="+str(num)
        suffix +="&category="+str(category)
        suffix +="&filter="+thefilter
        suffix +="&sortby="+sortby
        suffix +="&exclude_ports=8090,8123"
        resText = requests.get(self.API_url+suffix).text
        self.IP_list =resText.replace('\r','').split('\n')
        return self.IP_list
