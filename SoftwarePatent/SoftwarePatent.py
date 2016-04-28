__author__ = 'RealmL'
# encoding = UTF-8

import csv
import requests
from bs4 import  BeautifulSoup
import sys

try:
    from io import BytesIO as StringIO
except ImportError:
    try:
        from cStringIO import StringIO
    except ImportError:
        from io import StringIO

def get_html(company):
    # reload(sys)
    # sys.setdefaultencoding('utf8')
    url='http://www.chinacopyright.org.cn/findsoft.aspx#'
    header={
        'Host':' www.chinacopyright.org.cn',
        'Connection':' keep-alive',
        'Content-Length':' 140',
        'Accept':' application/json, text/javascript, */*',
        'Origin':' http://www.chinacopyright.org.cn',
        'X-Requested-With':' XMLHttpRequest',
        'User-Agent':' Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36',
        'Content-Type':' application/x-www-form-urlencoded',
        'Referer':' http://www.chinacopyright.org.cn/findsoft.aspx',
        'Accept-Encoding':' gzip, deflate',
        'Accept-Language':' zh-CN,zh;q=0.8',
        'Cookie':' bdshare_firstime=1461580381798; CNZZDATA1729576=cnzz_eid%3D732549115-1461576201-%26ntime%3D1461747035'
    }
    data={
        'softcopy':company#company.encode('gb2312')???
    }
    byhtml=requests.post(url=url,headers=header,data=data).content
    strhtml=byhtml.decode('utf-8')
    #print(strhtml)

    return strhtml

def get_patent(html):
    bs=BeautifulSoup(html,'html.parser')
    result_list=[]
    for tr in bs.find('form',{'method':'post','id':'form1'}).find('tbody').find_all('tr'):
        sub_list=[]
        for td in tr.find_all('td'):
            sub_list.append(td.string)
        sub_list.append(sub_list)
    return result_list

# def read_csv():
#
# def write_csv(data,name):
#     file_name = name
#     with open(file_name, 'a', errors='ignore', newline='') as f:
#         f_csv = csv.writer(f)
#         f_csv.writerows(data)


if __name__ == '__main__':
    html=get_html('百度')#虽然不用搜百度，主要是我随便试了几个他给的公司，都没有证书，有的不多
    #print(html.text)
    result_list=get_patent(html)
    print(result_list)

    # result_list.insert(0,('登记号','分类号','软件全称','软件简称','版本号','著作权人','批准日期'))
    # write_csv(result_list,r'res.csv')

