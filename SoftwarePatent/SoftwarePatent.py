__author__ = 'RealmL'
# coding = UTF-8

import csv
import requests
from bs4 import BeautifulSoup
import json

try:
    from io import BytesIO as StringIO
except ImportError:
    try:
        from cStringIO import StringIO
    except ImportError:
        from io import StringIO


def get_ResultList(company):
    url='http://www.chinacopyright.org.cn/findsoftjosn.aspx'
    data={
        'softcopy':company
    }
    JsonRes = requests.post(url=url,data=data)
    res = json.loads(JsonRes.text)
    #print(res)
    result_list=[]
    for i in res:
        #print(i)
        if i==None:
            result_list.append('没有找到相关的证书资料')
        else:
            sub_list=[]
            for value in i.values():
                #print(value)
                sub_list.append(value)
            result_list.append(sub_list)

    return result_list

# def get_patent(html):
#     bs=BeautifulSoup(html.text,'html.parser')
#     result_list=[]
#     for tr in bs.find('form',{'method':'post','id':'form1'}).find('div',{'id':'list'}).find('tbody').find_all('tr'):
#         sub_list=[]
#         for td in tr.find_all('td'):
#             sub_list.append(td.string)
#         sub_list.append(sub_list)
#     return result_list

def read_csv(name):
    reader = csv.reader(open(name, 'rb')) #二进制读取
    company_list=[]
    for line in reader:
        company_list.append(line.encode('utf-8'))

    return company_list

# def write_csv(data,name):
#     file_name = name
#     with open(file_name, 'a', errors='ignore', newline='') as f:
#         f_csv = csv.writer(f)
#         f_csv.writerows(data)


if __name__ =="__main__":
    company_list=read_csv('li.csv')
    print(company_list)
    # for company in company_list:
    #     result_list=get_ResultList(company)
    #     #print(result_list)
    #     write_csv(result_list,'res.csv')

