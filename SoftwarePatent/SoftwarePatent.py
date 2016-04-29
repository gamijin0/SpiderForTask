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
        if i['SoftID']!='0':
            sub_list=[]

            #for value in i.values():
                #print(value)
            sub_list.append(i['SoftID'])
            sub_list.append(i['TypeNum'])
            sub_list.append(i['SoftName'])
            sub_list.append(i['Verson'])
            sub_list.append(i['SoftAuthor'])
            sub_list.append(i['SuessDate'])
            sub_list.append(company)
            print(sub_list)
            result_list.append(sub_list)

        else:
            print(company+" 无数据.")

    return result_list



def read_csv(name):
        reader = csv.reader(open(name,'r',encoding='utf-8'))
        company_list=[]
        for line in reader:
            company_list.append(line[0])
        return company_list[1:]

def write_csv(data,name):
    file_name = name
    with open(file_name, 'a', errors='ignore', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)


if __name__ =="__main__":
    company_list=read_csv('li2.csv')
    #print(company_list)
    Suffix = [['登记号','分类号','软件名称','版本号','著作权人','批准日期','所属企业','公司名字']]

    write_csv(Suffix, 'res.csv')
    for company in company_list[120:]:
        try:
            result_list=get_ResultList(company)
        except:
            print("程序出现异常.")
        # result_list.insert(0,company)
        # print(result_list[0:10])
        write_csv(result_list,'res.csv')

