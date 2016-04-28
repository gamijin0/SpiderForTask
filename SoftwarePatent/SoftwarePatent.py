__author__ = 'RealmL'
# coding = UTF-8

import csv
import requests
from bs4 import  BeautifulSoup
import sys
import json

try:
    from io import BytesIO as StringIO
except ImportError:
    try:
        from cStringIO import StringIO
    except ImportError:
        from io import StringIO


def get_html(company):

    url='http://www.chinacopyright.org.cn/findsoftjosn.aspx'
    data = {
            'softcopy':company
        }

    JsonRes = requests.post(url=url,data=data)
    res = json.loads(JsonRes.text)
    print(res)

    for i in res:
        print(i)





if __name__ == '__main__':
    html=get_html('百度')#虽然不用搜百度，主要是我随便试了几个他给的公司，都没有证书，有的不多
    #print(html.text)
    #result_list=get_patent(html)
    #print(result_list)

    # result_list.insert(0,('登记号','分类号','软件全称','软件简称','版本号','著作权人','批准日期'))
    # write_csv(result_list,r'res.csv')

