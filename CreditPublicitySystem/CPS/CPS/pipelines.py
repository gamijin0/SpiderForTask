# -*- coding: utf-8 -*-
import json
import time
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
    corp_name = Column(String(40),primary_key=True)
    report_year = Column(Integer)
    capital_sum = Column(String(40))
    income_sum = Column(String(40))
    main_job_sum = Column(String(40))
    tax = Column(String(40))
    owner_rights = Column(String(40))
    profit_sum = Column(String(40))
    net_profit = Column(String(40))
    debt = Column(String(40))

engine = create_engine('mysql+mysqlconnector://root:xlsd1996@chaos.ac.cn:3306/CPS?charset=utf8')
DBSession = sessionmaker(bind=engine)
session = DBSession()
Base.metadata.create_all(engine)

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

        try:
            session.query(AnnualReport_db).filter_by(id=a_db.id).one()
            #若无异常,则说明数据库中已存在此对象
            print("\n\t数据库已存在[%s]" % str(a_db.id))

        except Exception as e:
            session.add(a_db)
            time.sleep(0.5)
            session.commit()
            print("\n已将[" + a['id'] + "]存入数据库\n")

        return a


