# -*- coding: utf-8 -*-
import scrapy
import time

class AnnualReportSpider(scrapy.spiders.Spider):
    name = "annual"
    url = 'http://www.jsgsj.gov.cn:58888/ecipplatform/nbServlet.json?nbEnter=true'

    def start_requests(self,id):

        data = {
            'ID': id,
            'OPERATE_TYPE': '2',
            'showRecordLine': '0',
            'specificQuery': 'gs_pb',
            'propertiesName': 'query_basicInfo',
            'tmp': str(time.strftime('%a+%b+%d+%Y+%H%%3A%M%%3A%S+GMT%%2B0800', time.localtime(time.time())))
        }