__author__ = 'Administrator'

import scrapy
from scrapy import Request
import json
import time
from ..items import Company,AnnualReport


class AnnualSpider(scrapy.Spider):

    name = 'AnnualReport'

    start=1
    end=1

    def __init__(self,start,end):
        super()
        self.start=start
        self.end=end

    def start_requests(self):
        # super.log.start(logfile="%s.log" % self.name)

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
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0'
        }

        annual_report_ids=[]

        #get ids from db
        # from ..pipelines import session,AnnualReport_db
        # annual_report_ids=session.query(AnnualReport_db.id).all()
        # print(annual_report_ids[0:10])

        #get ids from file
        import  csv
        import os
        with open(os.path.dirname(__file__)+"/../static/res_test.csv","r") as f:
            reader = csv.reader(f)
            for line in reader:
                annual_report_ids.append(line[0])

        ResList=[]


        for Id in annual_report_ids[int(self.start):int(self.end)]:
            data = {
                'ID': str(Id),
                'OPERATE_TYPE': '2',
                'showRecordLine': '0',
                'specificQuery': 'gs_pb',
                'propertiesName': 'query_basicInfo',
                'tmp': str(time.strftime('%a+%b+%d+%Y+%H%%3A%M%%3A%S+GMT%%2B0800', time.localtime(time.time())))
            }


            ResList.append(
                scrapy.FormRequest(
                    url=url,
                    headers=header,
                    formdata=data,
                    method='POST',
                    callback=self.GetAnnualReport,
                )
            )


        for r in ResList:
            print("Started:%s" % str(ResList.index(r)))
            yield r


    def GetAnnualReport(self,response):
        req_data = json.loads(response.body_as_unicode())[0]

        a = AnnualReport()
        try:
            a['id'] = str(req_data['ID'])
            a['corp_name'] = str(req_data['CORP_NAME'])
            a['report_year'] = str(req_data['REPORT_YEAR'])
            a['capital_sum'] = str(req_data['NET_AMOUNT'])
            a['income_sum'] = str(req_data['SALE_INCOME'])
            a['main_job_sum'] = str(req_data['SERV_FARE_INCOME'])
            a['tax'] = str(req_data['TAX_TOTAL'])
            a['owner_rights'] = str(req_data['TOTAL_EQUITY'])
            a['profit_sum'] = str(req_data['PROFIT_TOTAL'])
            a['net_profit'] = str(req_data['PROFIT_RETA'])
            a['debt'] = str(req_data['DEBT_AMOUNT'])

            #stock
            a['stock_name'] = str(req_data['STOCK_NAME'])
            a['change_before'] = str(req_data['CHANGE_BEFORE'])
            a['change_after'] = str(req_data['CHANGE_AFTER'])
            a['change_date'] = str(req_data['CHANGE_DATE'])
            print("\nFIND one:")
            yield a
            print("\n")
        except Exception as e:
            # print("Not this.")
            pass