# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import json
import time
from ..items import Company,AnnualReport
import requests

class CompanySpider(scrapy.spiders.Spider):



    name = 'Companys'

    url = 'http://www.jsgsj.gov.cn:58888/province/NoticeServlet.json?QueryExceptionDirectory=true'

    start_page =1
    end_page = 2

    def __init__(self,start_page,end_page):
        super()
        self.start_page = int(start_page)
        self.end_page = int(end_page)

    # 获取每个公司的年报列表
    def GetAnnuanlReportList(self, response):

        json_data = json.loads(response.body_as_unicode())['items']

        for i in json_data:
            com = Company()
            com['name'] = i['C1']
            com['reg_no'] = i['C2']
            #===============================================================
            #获得每个Company的AnnualReportList
            # 获取年报列表
            def get_annual_report_list(self):

                header = {
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

                url = 'http://www.jsgsj.gov.cn:58888/ecipplatform/nbServlet.json?nbEnter=true'

                data = {
                    'REG_NO': com['reg_no'],
                    'showRecordLine': "0",
                    'specificQuery': "gs_pb",
                    'propertiesName': "query_report_list",
                    'tmp': str(time.strftime('%a+%b+%d+%Y+%H%%3A%M%%3A%S+GMT%%2B0800', time.localtime(time.time())))
                }
                res_json = requests.post(url, headers=header, data=data).json()
                data.clear()
                com['annual_report_list']=[]
                for a in res_json:
                    aAnnual = AnnualReport()
                    aAnnual['id'] = a['ID']
                    com['annual_report_list'].append(aAnnual)
            #===============================================================

            get_annual_report_list(self)

            ResList=self.StartGetAnnualReport(com=com)
            for r in ResList:
                yield r

    # 开始获取公司列表
    def start_requests(self):

        for i in range(self.start_page, self.end_page):
            print("开始抓取第"+str(i)+"页\n")
            header = {
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

            data = {
                'showRecordLine': '1',
                'corpName': '',
                'tmp': str(time.strftime('%a+%b+%d+%Y+%H%%3A%M%%3A%S+GMT%%2B0800', time.localtime(time.time()))),
                'pageNo': str(i),
                'pageSize': '10'
            }


            MyRequest = scrapy.FormRequest(url=self.url,headers=header,method="POST",formdata=data,callback=self.GetAnnuanlReportList)

            yield MyRequest


    # 开始获取某个公司的年报
    def StartGetAnnualReport(self,com:Company):

        print("\n开始为公司%s抓取年报.\n" % com['name'])

        ResList =[]

        url = 'http://www.jsgsj.gov.cn:58888/ecipplatform/nbServlet.json?nbEnter=true'

        header = {
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

        #根据com['annual_report_list']发出多个请求
        for i in com['annual_report_list']:
            data = {
                'ID': str(i['id']),
                'OPERATE_TYPE': '2',
                'showRecordLine': '0',
                'specificQuery': 'gs_pb',
                'propertiesName': 'query_basicInfo',
                'tmp': str(time.strftime('%a+%b+%d+%Y+%H%%3A%M%%3A%S+GMT%%2B0800', time.localtime(time.time())))
            }

            ResList.append(scrapy.FormRequest(url=url,
                                 headers=header,
                                 formdata=data,
                                 method='POST',
                                 # callback= lambda annual_report=i:self.GetAnnualReport(annual_report),
                                 callback=lambda aAnnual=i:self.GetAnnualReport(aAnnual)
                                 ))
        return ResList

    # 获取某个公司的年报
    def GetAnnualReport(self,response,a:AnnualReport):

        req_data = json.loads(response.body_as_unicode())[0]

        # a = AnnualReport()
        a['capital_sum'] = str(req_data['NET_AMOUNT'])
        a['income_sum'] = str(req_data['SALE_INCOME'])
        a['main_job_sum'] = str(req_data['SERV_FARE_INCOME'])
        a['tax'] = str(req_data['TAX_TOTAL'])
        a['owner_rights'] = str(req_data['TOTAL_EQUITY'])
        a['profit_sum'] = str(req_data['PROFIT_TOTAL'])
        a['net_profit'] = str(req_data['PROFIT_RETA'])
        a['debt'] = str(req_data['DEBT_AMOUNT'])

        yield a


