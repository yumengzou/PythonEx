'''
Created on Jun 3, 2017

@author: yumeng.zou
'''
import numpy as np

## create an array
## array -- tuple of lists
## length fixed, content modifiable
arr1=np.array([[[1,1.5,2],[2,2.5,3],[3,3.5,4]],[[4,4.5,5],[5,5.5,6],[6,6.5,7]],[[7,7.5,8],[8,8.5,9],[9,9.5,10]],[[10,10.5,11],[11,11.5,12],[12,12.5,13]]])
arr2=np.zeros((4,3,3))
arr3=np.ones((4,3,3))
arr4=np.arange(16)
arr5=np.eye(5)
## print "{!r}\n\n{!r}\n\n{!r}\n\n{!r}\n\n{!r}".format(arr1,arr2,arr3,arr4,arr5)


## dtype and casting
## print(arr1.dtype)
int_arr1=arr1.astype(np.int32)
## print "{!r}\n\ncast it into np.int32\n{!r}".format(arr1, int_arr1)
str_arr1=arr1.astype(np.string_)
## print "\ncast it into np.string_\n{!r}\nits dimension = {}".format(str_arr1,str_arr1.shape)


## linear algebra on arr_matrix
arr0=np.arange(1,7,dtype=np.float64).reshape((2,3))
## print "{!r}\n\n{!r}\n\n{!r}".format(arr0+arr0,arr0**.5,1/arr0)


## Indexing & Slicing
## 1. Broadcast
arr6=np.arange(9)
arr6[5:8]=13
# print "{:10} :{}".format("Broadcast",repr(arr6))
arr2[:2]=9
# print "Multidimensional Broadcasting:\n",repr(arr2)

## 2. View
sliced_view=arr6[5:8]
# print "{:20} :{}".format("View of a slice", repr(sliced_view))
sliced_view[1]=64
# print "{:20} :{}".format("Change the slice",repr(arr6))

# indexing with slice
arr2_slice=arr2[1:3,1:3]
# print "{}\n{}".format("View of a Slice",repr(arr2_slice))
arr2_slice[:,1:]=3
# print "{}\n{}".format("Change the slice and you change everything",repr(arr2))


## 3. Matrix Indexing
# print "{:20} :{}".format("Standard Indexing",arr1[0][1][2])
# print "{:20} :{}".format("Matrix Indexing",arr1[0,1,2])


## 4. Boolean Indexing
names=np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print repr(names)
data=np.random.randn(7,4) ## random normal
print repr(data)
names_boo=(names=="Bob")
print repr(names_boo)
print repr(data[names=="Bob"])
print repr(data[names=="Bob",2:])

##### Eclipse is more suitable for object-oriented programming
##### Jupyter Notebook meet the purpose of data analysis better
##### I'll use Eclipse for exercises in the Hetland's book
##### and Jupyter Notebook for those in McKinney's
