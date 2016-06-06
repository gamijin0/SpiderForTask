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
    data= bs.find_all('div',{'class':'futureMarketBody'})
    for tr in data.find_all('tr'):
        if tr.find('td',{'class':'borderLeft'}).string=='2016-06-04':
            DayExchangeRate=tr.contents[1]
            TwoWeeksAvg=tr.contents[2]

    return DayExchangeRate,TwoWeeksAvg




if __name__ =="__main__":
    html=GetHtml()
    #print(html)
    DayExchangeRate,TwoWeeksAvg=GetIfo(html)
    print(DayExchangeRate)
    print(TwoWeeksAvg)

