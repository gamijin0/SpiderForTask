# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CpsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Company(scrapy.Item):
    name= scrapy.Field() #str
    reg_no = scrapy.Field() #str
    annual_report_list = scrapy.Field() #包含多个AnnualReport的list

class AnnualReport(scrapy.Item):
    corp_name =scrapy.Field()#str
    report_year = scrapy.Field()#int
    id = scrapy.Field() #str
    report_name = scrapy.Field() #str
    capital_sum = scrapy.Field() #str
    income_sum = scrapy.Field() #str
    main_job_sum =scrapy.Field() #str
    tax = scrapy.Field() #str
    owner_rights =scrapy.Field() #str
    profit_sum = scrapy.Field() #str
    net_profit = scrapy.Field() #str
    debt =scrapy.Field() #str

    stock_name=scrapy.Field() #str
    change_before=scrapy.Field() #str
    change_after=scrapy.Field() #str
    stockright_change_date=scrapy.Field() #str