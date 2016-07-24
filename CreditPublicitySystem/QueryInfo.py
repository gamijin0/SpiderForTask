__author__ = 'RealmL'

import requests
import csv
import json
import time
import random
from CreditPublicitySystem.Company import company,annual_report


from bs4 import BeautifulSoup



class CreditPublicitySystem(object):

    Company_list=[]

    #打印当前数据
    def Print_List(self):
            for c in self.Company_list:
                print(c)


    def __init__(self):
        self.header = {
            'Host': 'www.jsgsj.gov.cn:58888',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'http://www.jsgsj.gov.cn:58888/province/notice/QueryExceptionDirectory.jsp',
            # 'Content-Length': '91',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0'
        }
        self.Company_list=[]

    #获取公司列表
    def get_company_list(self, page_number: int):
        url = 'http://www.jsgsj.gov.cn:58888/province/NoticeServlet.json?QueryExceptionDirectory=true'
        data = {
            'showRecordLine': '1',
            'corpName': '',
            'tmp': str(time.strftime('%a+%b+%d+%Y+%H%%3A%M%%3A%S+GMT%%2B0800', time.localtime(time.time()))),
            'pageNo': str(page_number),
            'pageSize': '10'
        }
        request_data = (requests.post(url, headers=self.header, data=data, timeout=10)).json()
        json_data = request_data['items']

        for i in json_data:
            tmp =company(i['C1'],i['C2'])
            self.Company_list.append(tmp)

    #获取年报
    def __get_report(self,a:annual_report):
        url='http://www.jsgsj.gov.cn:58888/ecipplatform/nbServlet.json?nbEnter=true'
        data={
            'ID':a.id,
            'OPERATE_TYPE':'2',
            'showRecordLine':'0',
            'specificQuery':'gs_pb',
            'propertiesName':'query_basicInfo',
            'tmp':str(time.strftime('%a+%b+%d+%Y+%H%%3A%M%%3A%S+GMT%%2B0800', time.localtime(time.time())))
        }
        req_data=requests.post(url=url,headers=self.header,data=data).json()
        req_data = req_data[0]
        a.capital_sum=req_data['NET_AMOUNT']
        a.income_sum=req_data['SALE_INCOME']
        a.main_job_sum=req_data['SERV_FARE_INCOME']
        a.tax=req_data['TAX_TOTAL']
        a.owner_rights=req_data['TOTAL_EQUITY']
        a.profit_sum=req_data['PROFIT_TOTAL']
        a.net_profit=req_data['PROFIT_RETA']
        a.debt=req_data['DEBT_AMOUNT']

        # a.shareholder=req_data['']
        # a.before_percent=req_data['']
        # a.after_percent=req_data['']
        # a.share_change_date =req_data['']
        #
        # a.change_item=req_data['']
        # a.change_before=req_data['']
        # a.change_after=req_data['']
        # a.change_date =req_data['']
        #
        # a.zhaiquanren =req_data['']
        # a.zhaiwren=req_data['']
        # a.zhaiquanzhonglei =req_data['']
        # a.zhaiquanshue =req_data['']
        # a.zhaiwuqixian =req_data['']
        # a. baozhengqijian =req_data['']
        # a.baozhengfangshi=req_data['']


    #获取年报列表
    def get_annual_report(self):
        # self.header['Content-Length'] = '136'
        url='http://www.jsgsj.gov.cn:58888/ecipplatform/nbServlet.json?nbEnter=true'

        for c in self.Company_list:
            data={
                'REG_NO':c.reg_no,
                'showRecordLine':"0",
                'specificQuery':"gs_pb",
                'propertiesName':"query_report_list",
                'tmp':str(time.strftime('%a+%b+%d+%Y+%H%%3A%M%%3A%S+GMT%%2B0800', time.localtime(time.time())))
            }
            time.sleep(0.5)
            res_json = requests.post(url, headers=self.header, data=data).json()
            data.clear()
            for a in res_json:
                tmp_a = annual_report(a['ID'])
                tmp_a.report_name = a['REPORT_RESULT']
                self.__get_report(tmp_a)
                c.annual_report_list.append(tmp_a)






# def write_to_csv(file_name, data):
#     with open(file_name, 'a', newline='', encoding='utf-8') as fp:
#         fp_csv = csv.writer(fp)
#         fp_csv.writerows(data)


if __name__ == '__main__':
    from CreditPublicitySystem.CPS.CPS.pipelines import AnnualReport_db
    from sqlalchemy import Column, String, create_engine, Integer
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base
    engine = create_engine('mysql+mysqlconnector://root:xlsd1996@chaos.ac.cn:3306/CPS?charset=utf8')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    res = session.query(AnnualReport_db).filter_by(id="1004699887").one()
    print(res.id,res.corp_name)
    session.close()
    # cps = CreditPublicitySystem()
    # cps.get_company_list(1)
    # cps.get_annual_report()
    # cps.Print_List()

    # print(company_list)
    # for company in company_list:
    #     print(test.get_company_annual_report_info(company))

    # write_to_csv('经营异常信息.csv', [['企业名称', '列入经营异常名录原因', '列入日期', '移出经营异常名录原因', '移出日期',
    #                              '作出决定机关']])
    # for number in range(1,2):
    #     while True:
    #         try:
    #             company_list = test.get_company_list(number)
    #             page_data = []
    #             for company in company_list:
    #                 while True:
    #                     try:
    #                         page_data.extend(test.get_company_annual_report_info(company))
    #                     except Exception:
    #                         continue
    #                     print('\t', company['C1'], 'success')
    #                     break
    #             # write_to_csv('经营异常信息2000-2999.csv', page_data)
    #             print('page', number, 'success')
    #             break
    #         except Exception:
    #             continue