__author__ = 'RealmL'
# coding = UTF-8

import requests
from bs4 import BeautifulSoup as BS

# 解决编码问题
try:
    from io import BytesIO as StringIO
except ImportError:
    try:
        from cStringIO import StringIO
    except ImportError:
        from io import StringIO


def  GetHtml( ):
    url='https://www.okcoin.com/future/market.do?index=0'
    header={
        'Host':"www.okcoin.com",
        'User-Agent':"Mozilla/5.0 (Windows NT 6.1; rv:46.0) Gecko/20100101 Firefox/46.0",
        'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        'Accept-Language':"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        'Accept-Encoding':"gzip, deflate, br",
        'Referer':"https://www.okcoin.com/future/market.do?index=0"
    }
    response=requests.get(url=url,headers=header)
    html=response.text
    return html

def GetIfo(html):
    bs = BS(html,"html.parser")
    data= bs.find_all('div',{'class':'futureMarkBody'})


    for tr in data[1].find_all('tr'):
        #print(tr.contents)
        if '2016-06-04' in str(tr):
            DayExchangeRate=tr.contents[3].string
            TwoWeeksAvg=tr.contents[5].string

    return DayExchangeRate,TwoWeeksAvg




if __name__ =="__main__":
    html=GetHtml()
    #print(html)
    print(GetIfo(html))

