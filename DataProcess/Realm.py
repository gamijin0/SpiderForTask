import csv

def OpenFile(fileName):
    with open(fileName,mode='rb') as f:
        reader = f.readlines()
        return reader

def SaveFile(fileName,data):
    with open(fileName,mode='w') as f:
        writer = csv.writer(f)
        writer.writerows(data)


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
            res.append((i,"No 创始人"))
            continue
        else:
            if(data.find("◎")!=-1 or data.find("。")!=-1):
                if(data.find("◎")!=-1):
                    temp = data.split("◎")
                if(data.find("。")!=-1):
                    temp = data.split("。")

                data=""
                for div in temp:
                    if(div.find("创始人")!=-1):
                        data+=div
                        if(div.find(creater)!=-1): #如果项目负责人是创始人
                            data = ""
                            for div2 in temp:
                                if(div.find(creater)!=1):
                                    data+=div
                            break

                res.append((i,data))
                pass
            else:
                res.append((i, "No division."))
                continue

    for i in res:
        print(i)

    SaveFile("test.csv",res)