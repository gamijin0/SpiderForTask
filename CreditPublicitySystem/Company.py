__author__ = 'Administrator'

class annual_report:
    id=str()
    report_name=str()
    capital_sum =str()
    income_sum = str()
    main_job_sum = str()
    tax = str()
    owner_rights = str()
    profit_sum=str()
    net_profit=str()
    debt = str()

    # shareholder = str()
    # before_percent=str()
    # after_percent =str()
    # share_change_date = str()
    #
    # change_item = str()
    # change_before=str()
    # change_after=str()
    # change_date = str()
    #
    # zhaiquanren = str()
    # zhaiwren=str()
    # zhaiquanzhonglei = str()
    # zhaiquanshue =str()
    # zhaiwuqixian = str()
    # baozhengqijian =str()
    # baozhengfangshi=str()


    def __init__(self,id:str):
        self.id = id
    def __str__(self):
        res = ""
        for v in vars(self):
            # if(v.__len__()>0):
            res+="\n\t\t["+v+":"+str(self.__getattribute__(v))+"]"
        return res

class company(object):

    name =str()
    reg_no = str()
    annual_report_list =[]

    def __str__(self):
            res = "\n公司名称:"+self.name+" 年报:["
            for a in self.annual_report_list:
                res+="\t\n"+str(a)
            res+="\n]\n"
            return res


    def __init__(self,name,reg_no):
        self.name = name
        self.reg_no = reg_no
        self.annual_report_list =[]



