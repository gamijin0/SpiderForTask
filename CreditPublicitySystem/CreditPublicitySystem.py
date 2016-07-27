__author__ = 'rachin'

import requests
import csv
import json
import time
import random
from bs4 import BeautifulSoup


class CreditPublicitySystem(object):
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
            'Content-Length': '91',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0'
        }

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
        #print(request_data)
        json_data = request_data['items']
        return json_data

    def get_company_annual_report_info(self, json_data: dict):
        self.header['Content-Length'] = '136'
        url='http://www.jsgsj.gov.cn:58888/ecipplatform/nbServlet.json?nbEnter=true'
        data={
            'REG_NO':json_data['C2'],
            'showRecordLine':"0",
            'specificQuery':"gs_pb",
            'propertiesName':"query_report_list",
            'tmp':str(time.strftime('%a+%b+%d+%Y+%H%%3A%M%%3A%S+GMT%%2B0800', time.localtime(time.time())))
        }
        request_data = requests.post(url, headers=self.header, data=data).json()
        result_data = []
        result_data.append(json_data['C1'])
        if request_data.__len__()==0:
            result_data.append('无企业年报 ')
        else:
            # print(request_data)
            result_data.extend(request_data)
        return result_data



    # def get_abnormal_information_management(self, json_data: dict):
    #     url = 'http://www.jsgsj.gov.cn:58888/ecipplatform/commonServlet.json?commonEnter=true'
    #     self.header['Content-Length'] = '180'
    #     data = {
    #         'showRecordLine': '1',
    #         'specificQuery': 'commonQuery',
    #         'propertiesName': 'abnormalInfor',
    #         'corp_org': str(json_data['CORP_ORG']),
    #         'corp_id': str(json_data['CORP_ID']),
    #         'corp_seq_id': str(json_data['SEQ_ID']),
    #         'tmp': str(time.strftime('%a+%b+%d+%Y+%H%%3A%M%%3A%S+GMT%%2B0800', time.localtime(time.time()))),
    #         'pageNo': '1',
    #         'pageSize': '5'
    #     }
    #     #time.sleep()
    #     try:
    #         request_data = requests.post(url, headers=self.header, data=data, timeout=10).json()
    #         json_data_now = request_data['items']
    #         result_data = []
    #         for each in json_data_now:
    #             temp = [json_data['C1']]
    #             for key in ['C1', 'C2', 'C3', 'C4', 'C5']:
    #                 temp.append(each[key])
    #             result_data.append(temp)
    #     except Exception:
    #         raise Exception
    #     return result_data


# def write_to_csv(file_name, data):
#     with open(file_name, 'a', newline='', encoding='utf-8') as fp:
#         fp_csv = csv.writer(fp)
#         fp_csv.writerows(data)


if __name__ == '__main__':
    test = CreditPublicitySystem()
    company_list=test.get_company_list(1)
    for company in company_list:
        print(test.get_company_annual_report_info(company))

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