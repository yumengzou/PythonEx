'''
Created on Jun 3, 2017

@author: yumeng.zou
'''
##### String Constant #####
import string
string.digits
string.punctuation
string.printable

##### String Methods #####

s="Say something, I'm giving up on you"

## .find(str)
s.find("I'm")    ## find a substring within a larger string
s.find("y")      ## return the leftest index
s.find("wulala") ## return -1 if not found

## .join(sequence)
sep="+"
seq=["1","2","3","4","5"]
sep.join(seq)    ## inverse of .split()

directory=("","User","yumeng.zou","pycoding")
"/".join(directory)

## .title()
## .replace(old_str, new_str)
import glob,os
path="/Users/yumeng.zou/Documents/shakespeare/*.txt"
filenames=glob.glob(path)
clean_filenames=[os.path.split(f)[1][:-4].replace("_", " ").title() for f in filenames]
## .title() <- .split()+.upper()+.join()

## capwords(str)
from string import capwords
capwords(s)
string.capwords(s)

## .split()

## .strip()

## .translate(dict)
    ## .maketrans(from_str, to_str)
    ## one-to-one substitution
    ## return a dictionary
d=s.maketrans("kstr","gzdl")

s="This is a man's world"
s.translate(d)
ss="but there'll be nothing without a woman or a girl"
ss.translate(d)