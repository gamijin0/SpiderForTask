__author__ = 'Guo'
# coding: utf-8
import requests
from bs4 import BeautifulSoup
import time
import random
import socket

try:
    from io import BytesIO as StringIO
except ImportError:
    try:
        from cStringIO import StringIO
    except ImportError:
        from io import StringIO
#  实行翻页并获取html
class Get_pages(object):

    def get_html(self,start,proxies):
        time.sleep(0.1*random.choice(range(1,3)))
        header = {
            'Host':"www.pss-system.gov.cn",
            'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
            'Accept':"text/html, */*",
            'Accept-Encoding':"gzip, deflate"

        }
        session = requests.session()
        session.proxies = proxies
        '''
        proxies = {
            'http':'113.30.102.91:3128',
            'https':'113.30.102.91:3128'
        }
        '''
        #

        form = {
            'resultPagination.limit':"10",
            'resultPagination.sumLimit':"10",
            'resultPagination.start':str(start),
            'resultPagination.totalCount':"9695384",
            'searchCondition.searchType':"Sino_foreign",
            'searchCondition.dbId': "",
            'searchCondition.strategy':"",
            'searchCondition.literatureSF':"",
            # 'resultPagination.sumLimit':"10,10,10,10,10,10,10,10,10,10,10,10,10",
            'searchCondition.searchExp':"公司",
            'wee.bizlog.modulelevel':"0200101",
            'searchCondition.executableSearchExp':"VDB:(IBI='公司')",
            'searchCondition.searchKeywords':"",
            'searchCondition.searchKeywords':"[公][+]{0,}[司][+]{0,}"
        }
        url = 'http://www.pss-system.gov.cn/sipopublicsearch/search/showSearchResult-startWa.shtml'
        while True:
            try:
                html =session.post(url,data=form,headers = header,timeout = 7)
                break

            except socket.timeout as e:
                print(2,e)
            except requests.exceptions.ConnectTimeout as e :
                print(1,e)
                return ''
            except requests.exceptions.ReadTimeout as e :
                print(3,e)
                return ''
            except requests.exceptions.ConnectionError as e:
                print(4,e)
                return ''
            except Exception as e:
                print(5,e)
                return ''

        # print(html.text)
        #bs = BeautifulSoup(html.text)
        #print(bs.title.get_text())


        return html.text


if __name__ == '__main__':
    pages = Get_pages()
    print(pages.get_html(10))
