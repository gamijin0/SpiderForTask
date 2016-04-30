import time
import os

step = 100000
for i in range(0,6*step,step):
    print("[%d~%d]已开始." % (i,i+step-1))
    os.popen("python3 ./main.py %d %d > log" % (i,i+step-1) )
    time.sleep(1)

#os.system("python ./main.py 1 20 ")
