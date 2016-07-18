# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import json
import time
from ..items import Company
import requests

class CompanySpider(scrapy.spiders.Spider):



    name = 'Companys'

    url = 'http://www.jsgsj.gov.cn:58888/province/NoticeServlet.json?QueryExceptionDirectory=true'



    page_num =1
    end_page = 2

    def __init__(self,start_page,end_page):
        super()
        self.page_num = int(start_page)
        self.end_page = int(end_page)

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
                    com['annual_report_list'].append(str((a['ID'])))

            #===============================================================

            get_annual_report_list(self)

            # filename = "CompanyList.txt"
            # with open(filename, 'wb') as f:
            #     f.write(response.body)

            yield com

            yield self.start_requests()

    def start_requests(self):

        if(self.page_num>self.end_page):
            print("抓取结束.")
            return None

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
            'pageNo': str(self.page_num),
            'pageSize': '10'
        }


        MyRequest = scrapy.FormRequest(url=self.url,headers=header,method="POST",formdata=data,callback=self.GetAnnuanlReportList)

        self.page_num += 1

        return [MyRequest]