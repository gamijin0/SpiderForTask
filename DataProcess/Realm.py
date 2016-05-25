import csv


def OpenFile(fileName):
    with open(fileName,mode='rb') as f:
        reader = f.readlines()
        return reader

def SaveFile(fileName,data):
    with open(fileName,mode='w') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False



if(__name__=='__main__'):
    reader = OpenFile("original_data(1).csv")
    res = list()
    i=-1
    for line in reader:
        i+=1
        if(i==0):
            continue
        creater = line.decode('gbk').split(',')[8]
        data = line.decode('gbk').split(',')[9]
        #print(data.find("创始人"))
        if(data.find("创始人")==-1):
            res.append([i,"No Creeater"])   #!!!
            continue
        else:
            if(data.find("◎")!=-1 or data.find("。")!=-1):
                temp1 = data.split("◎")
                temp2=list()
                for t in temp1:
                    temp2 +=t.split("。")

                temp = temp2
                data=""
                for div in temp:
                    if(div.find("创始人")!=-1):
                        if(data!=""):
                            data+="，"
                        data+=div

                        if(div.find(creater)!=-1): #如果项目负责人是创始人
                            data = ""
                            for div2 in temp:
                                if(div2.find(creater)!=-1):
                                    if(data!=""):
                                        data+="，"
                                    data+=div2
                            break

                res.append([i,data])
                pass
            else:
                res.append([i, "No division."])
                continue

    for line in res:
        print(line[0])
        JudgeList=("大学","学院","本科","研究生","博士")
        JudgeRes = list()
        for j in JudgeList:
            JudgeRes.append(line[1].find(j))
        #print(JudgeRes)
        bk=ss=bs="0"
        for jRes in JudgeRes:
            if(jRes!=-1):
                tempXueli1=tempXueli2=""
                Mstart = line[1][:jRes]
                for uchar in Mstart[::-1]:
                    if(is_chinese(uchar) or uchar=="、" or "1234567890".find(uchar)!=-1):
                        tempXueli1+=uchar
                    else:
                        break
                Mend = line[1][jRes:]
                for uchar in Mend:
                    if(is_chinese(uchar) or uchar=="、"):
                        tempXueli2+=uchar
                    else:
                        break
                if(JudgeRes.index(jRes)==0 or JudgeRes.index(jRes)==1 or JudgeRes.index(jRes)==2):
                    bk=tempXueli1[::-1]+tempXueli2
                if(JudgeRes.index(jRes)==3):
                    ss=tempXueli1[::-1]+tempXueli2
                if(JudgeRes.index(jRes)==4):
                    bs=tempXueli1[::-1]+tempXueli2

        line.append("本科:"+bk)
        line.append("硕士:"+ss)
        line.append("博士:"+bs)

        #del(line[1])
        print(line)
    SaveFile("test.csv",res)


