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
    id = scrapy.Field() #str