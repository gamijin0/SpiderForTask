__author__ = 'Administrator'

import scrapy
from scrapy import Request
import json
import time
from ..items import Company,AnnualReport


class AnnualSpider(scrapy.Spider):

    super.name = 'AnnualReport'

    def start_requests(self):
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


        from ..pipelines import session,AnnualReport_db
        annual_report_ids=session.query(AnnualReport_db.id).all()

        ResList=[]

        for Id in annual_report_ids:
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
        return ResList


    def GetAnnualReport(self,response):
        req_data = json.loads(response.body_as_unicode())[0]

        a = AnnualReport()
        a['id']=str(req_data['ID'])


        yield a
