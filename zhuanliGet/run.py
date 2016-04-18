import time
import os


for i in range(300000,500000,10000):
    print("[%d~%d]已开始." % (i+1,i+10000))
    os.popen("python ./main.py %d %d > log" % (i+1,i+10000) )
    time.sleep(1)

#os.system("python ./main.py 1 20 ")
