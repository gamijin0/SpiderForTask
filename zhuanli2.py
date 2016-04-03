__author__ = 'Guo'
# coding: utf-8
import requests
from bs4 import BeautifulSoup
import time
import random
import re

# 从html中获取数据
class  Get_content(object):

    def get_content(self,html):
        result = []
        soup = BeautifulSoup(html)
        for i in range(0,10):
            temp = []
            id = "sameApDiv" + str(i)
            div = soup.find('div',{'id': str(id)})
            # print(div)
            try:
                td = div.find_all('td',{'valign': "top"})
                # print(td)

                application_number = application_date = open_date = name_of_invention = IPC_classification_number = ' '
                applicant = inventor = priority_number = priority_day = agent = agency = appearance_design_of_Luojianuo_classification_number = ' '
                for i in td:
                    try:
                        contents = i.contents
                        if (contents[1].next == "申请号­: "):
                            application_number = i.contents[2]
                            p=re.compile('\s+')
                            application_number=re.sub(p,'',application_number)

                        elif(contents[1].next == "申请日: "):
                            application_date = i.contents[2]
                            p=re.compile('\s+')
                            application_date=re.sub(p,'',application_date)

                        elif(contents[1].next == "公开（公告）号­: "):
                            open_number = i.contents[2]
                            p=re.compile('\s+')
                            open_number=re.sub(p,'',open_number)

                        elif(contents[1].next == "公开（公告）日: "):
                            open_date = i.contents[2]
                            p=re.compile('\s+')
                            open_date=re.sub(p,'',open_date)

                        elif(contents[1].next == "发明名称: "):
                            name_of_invention = i.contents[2]
                            p=re.compile('\s+')
                            name_of_invention=re.sub(p,'',name_of_invention)
                        #elif(contents[1].next == "IPC分类号: "):
                        #   IPC_classification_number = i.contents[2]
                        elif(contents[1].next == "申请（专利权）人: "):
                            applicant = i.contents[2]
                            p=re.compile('\s+')
                            applicant=re.sub(p,'',applicant)

                        elif(contents[1].next == "发明人: "):
                            inventor = i.contents[2]
                            p=re.compile('\s+')
                            inventor=re.sub(p,'',inventor)

                        elif(contents[1].next == "优先权号: "):
                            priority_number = i.contents[2]
                            p=re.compile('\s+')
                            priority_number=re.sub(p,'',priority_number)

                        elif(contents[1].next == "优先权日: "):
                            priority_day = i.contents[2]
                            p=re.compile('\s+')
                            priority_day=re.sub(p,'',priority_day)

                        elif(contents[1].next == "代理人: "):
                            agent = i.contents[2]
                            p=re.compile('\s+')
                            agent=re.sub(p,'',agent)

                        elif(contents[1].next == "代理机构: "):
                            agency = i.contents[2]
                            p=re.compile('\s+')
                            agency=re.sub(p,'',agency)

                        elif(contents[1].next == "外观设计珞珈诺分类号: "):
                            appearance_design_of_Luojianuo_classification_number = i.contents[2]
                            p=re.compile('\s+')
                            appearance_design_of_Luojianuo_classification_number=re.sub(p,'',appearance_design_of_Luojianuo_classification_number)

                        else:
                            continue
                    except:
                        continue

                temp.extend([application_number,application_date,open_number,open_date,name_of_invention,applicant,inventor,priority_number,priority_day,appearance_design_of_Luojianuo_classification_number,agent,agency])
                result.append(temp)
            except:
                continue
        return result


if __name__ == '__main__':
    co = Get_content()
    # co.get_content(html)


