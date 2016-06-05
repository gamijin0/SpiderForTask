__author__ = 'RealmL'
# coding = UTF-8

import  csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

def ReadCSV(filename):
    """
     @description： 读取CSV文件
    @parameter： 文件名称
    @return: 返回读取数据的一个列表
    """
    f_csv  = csv.reader(open(filename,'r',encoding='utf-8'))
    data = []
    for row in f_csv:
        if f_csv.line_num == 1:
            continue
        data.append(row)
    return data

def WriteCSV(filename,data):
    """
     @description： 将数据写入CSV文件
    @parameter1： 文件名称
    @parameter2:    需写入的数据
    @return：None
    """
    with open(filename,'a',newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)

def TrainingDataProcessing(data):
    """
     @description： 对数据进行预处理，包括缺失值处理及数据标准化
    @parameter1： 需处理的数据
    @return：返回处理后的数据（一个二维数组）
    """
    TrainingDataList = []
    for row in data:
        TrainingDataList.append([float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]),float(row(7))])

    TrainingDataArray = np.array(TrainingDataList)
    min1 = np.min(np.array([x for x in TrainingDataArray[:, 3:4] if x!=0]))#缺失值处理,将零值用非零值的最小值代替
    min2 = np.min(np.array([x for x in TrainingDataArray[:, 4:5] if x!=0]))
    for i, row in enumerate(TrainingDataArray):
        if row[3] == 0:
            TrainingDataArray[i][3] = min1
        if row[4] == 0:
           TrainingDataArray[i][4] = min2

    ScaledData = preprocessing.scale(TrainingDataArray[:,0])#标准化
    for i in range(1, 5):
        ScaledData = np.column_stack((ScaledData,preprocessing.scale(TrainingDataArray[:, i])))

    return ScaledData

if __name__=='__main__':
    Data = ReadCSV('training_data.csv')
    X = TrainingDataProcessing(Data)
    n_clusters=10#聚成10簇
    model = KMeans(n_clusters=n_clusters)
    model_predict = model.fit_predict(X)

    data = np.array(Data)
    plt.figure(figsize=(16, 16))#散点图
    plt.subplot(221)
    plt.scatter(data[:, 0], data[:, 1], c=model_predict)
    plt.title("MaxShareHoldingProportion")
    plt.subplot(222)
    plt.scatter(data[:, 0], data[:, 2], c=model_predict)
    plt.title("NumberOfTeams")
    plt.subplot(223)
    plt.scatter(data[:, 0], data[:, 3], c=model_predict)
    plt.title("RegisteredCapital")
    plt.subplot(224)
    plt.scatter(data[:, 0], data[:, 6], c=model_predict)
    plt.title("EducationBackgroundCreditOfCreator")
    plt.show()
    plt.subplot(221)
    plt.scatter(data[:, 0], data[:, 7], c=model_predict)
    plt.title("CareerCreditOfCreator")
    plt.show()#显示所有子图

    WriteCSV('res_data1.csv', np.column_stack((data[:, 0], model_predict)))








