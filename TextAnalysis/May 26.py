##### Data Structure - Sequence #####
# Indexing
# Slicing [start:stop:step]
# Adding
# Multiplication
l=[1,2,3]
l*3
## >>> [1,2,3,1,2,3,1,2,3]
# Membership
list=[1,2,3]
1 in list
## >>> True
4 in list
## >>> False
len(list)
min(list)
max(list)
lst=range(10)
## Error
## in Python 3 range is not a function but an immutable sequence type
lst=list(range(10))
## convert a range into a list with a list function
lst.append(3)
lst.count(3)
lst.extend([11,12,13])
lst.index(3)
lst.insert(10, "ten")
lst.pop(11)
