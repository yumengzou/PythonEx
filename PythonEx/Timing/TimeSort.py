'''
Created on Jul 22, 2017

@author: yumeng.zou
'''
import timeit
import numpy as np
import random
from Sorting import *
import os

os.chdir("/Users/yumeng.zou/Google Drive/Freshyear/Summer/Algorithm/")

Methods=['insert_sort','recursive_insert_sort','select_sort','merge']

f=open("sort.txt",'w')
f.write("length,"+','.join(Methods)+"\n")

Testers=[]
for i in np.arange(1,21):
    tester=np.arange(5*i)
    random.shuffle(tester)
    Testers.append(tester)

for method in Methods:
    for tester in Testers:
        toSort=tester
        if method=='merge':
            s=method+"(toSort,0,len(toSort))"
        else:
            s=method+"(toSort)"
        t=timeit.timeit(s,globals=globals(),number=10000)
        print(t)
        f.write(str(len(tester))+','+str(t)+'\n')
    f.write("\n")
f.close()



