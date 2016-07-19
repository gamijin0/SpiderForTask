# -*- coding: utf-8 -*-
import json
from .items import AnnualReport
from sqlalchemy import Column, String, create_engine,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class AnnualReport_db(Base):
    # 表的名字:
    __tablename__ = 'annual_report'

    # 表的结构:
    id = Column(String(40), primary_key=True)
    corp_name = Column(String(40))
    report_year = Column(Integer)
    capital_sum = Column(String(40))
    income_sum = Column(String(40))
    main_job_sum = Column(String(40))
    tax = Column(String(40))
    owner_rights = Column(String(40))
    profit_sum = Column(String(40))
    net_profit = Column(String(40))
    debt = Column(String(40))

engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
DBSession = sessionmaker(bind=engine)
session = DBSession()

class CpsPipeline(object):
    #写入数据库
    def process_item(self, a:AnnualReport, spider):

        a_db = AnnualReport_db()
        a_db.id=a['id']
        a_db.corp_name=a['corp_name']
        a_db.report_year=a['report_year']
        a_db.capital_sum=a['capital_sum']
        a_db.income_sum=a['income_sum']
        a_db.main_job_sum=a['main_job_sum']
        a_db.tax=a['tax']
        a_db.owner_rights=a['owner_rights']
        a_db.profit_sum=a['profit_sum']
        a_db.net_profit=a['net_profit']
        a_db.debt=a['debt']

        session.add(a_db)
        session.commit()


        return a
