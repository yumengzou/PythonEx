'''
Created on Jun 22, 2017

@author: yumeng.zou
'''

import random
import numpy as np


def insert_sort(arr):
    for i in np.arange(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]: # reverse loop over subarray A[:i]
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key               # while/else
                
lo=range(20)
random.shuffle(lo)
print "{:10}{}".format("unsorted", lo)
insert_sort(lo)          
print "{:10}{}\n".format("sorted", lo)



def recursive_insert_sort(arr):
    if len(arr)==1:
        return
    recursive_insert_sort(arr[:-1])
    insert_sort(arr)

a=np.arange(20)
random.shuffle(a)
print "{:10}{}".format("unsorted", a)
recursive_insert_sort(a)
print "{:10}{}\n".format("recursive_insert", a)    



def reverse_insert_sort(lst):
    for i in np.arange(1,len(lst)):
        key=lst[i]
        j=i-1
        while j>=0 and key>lst[j]:
            lst[j+1]=lst[j]
            j-=1
        lst[j+1]=key

random.shuffle(lo)
print "{:10}{}".format("unsorted", lo)
reverse_insert_sort(lo)
print "{:10}{}\n".format("reverse", lo)



def linear_search(arr,v):
    for i,n in enumerate(arr):
        if n==v:
            return i
    return "None"

random.shuffle(a)
print "{:10}{}".format("array", a)
print "{:10}{}".format("index of 7: ", linear_search(a,7))
print "{:10}{}\n".format("index of 21: ", linear_search(a,21))



def binary_search(arr,v):
    start=0
    end=len(arr)
    while start<end-1:
        mid=int((start+end)/2)
        if arr[mid]==v:
            return mid
        if arr[mid]>v:
            end=mid
        if arr[mid]<v:
            start=mid
    return None
        
random.shuffle(a)
print "{:10}{}".format("array", a)
print "{:10}{}".format("bs_index of 7: ", binary_search(a,7))
print "{:10}{}\n".format("bs_index of 21: ", binary_search(a,21))



def binary_sum(bin1,bin2):
    n=max(len(bin1),len(bin2))+1
    ans=np.zeros(n)
    #print(np.arange(-1,-n,-1))
    for i in np.arange(-1,-n,-1):
        if (bin1[i]+bin2[i]+ans[i]==1):
            ans[i]=1
        elif (bin1[i]+bin2[i]+ans[i]==2):
            ans[i]=0
            ans[i-1]+=1
        elif (bin1[i]+bin2[i]+ans[i]==3):
            ans[i]=1
            ans[i-1]+=1
    return ans

b1=[1,0,1,1,0,0]
b2=[0,1,1,1,1,0]
print "{:10} b1{} and b2{} is {}\n".format("sum of", b1, b2, binary_sum(b1, b2))



def select_sort(arr):
    for i in np.arange(0,len(arr)-1):
        x=j=i
        while j<len(arr):
            if arr[j] < arr[x]:
                x=j
            j+=1
        arr[i],arr[x]=arr[x],arr[i]
    return arr

random.shuffle(a)
print "{:10}{}".format("unsorted", a)
print "{:10}{}\n".format("select_insert", select_sort(a))



def merge_sort(arr,p,q,r):  # p<=q<r are indices in arr
    left=np.append(arr[p:q],np.inf)  # infinity as sentinels
    right=np.append(arr[q:r],np.inf)
#     print left,right
    i=j=0
    for k in np.arange(p,r):
#         if i>=len(left):
#             arr[k:r]=right[j:]
#             break
#         elif j>=len(right):
#             arr[k:r]=left[i:]
#             break
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
    return arr

b=np.arange(6)
random.shuffle(b)
print "{:10}{}".format("unsorted", b)
print "{:10}{}\n".format("merge_sort", merge_sort(b,0,3,6))
            


def merge(arr,p,r):
    if len(arr[p:r])==1:
        return arr
    else:
        q=(p+r)/2
        merge(arr,p,q)
        merge(arr,q,r)
        merge_sort(arr, p, q, r)
        return arr
    
random.shuffle(a)
print "{:10}{}".format("unsorted", a)
merge(a,0,20)
print "{:10}{}\n".format("merge", a)



