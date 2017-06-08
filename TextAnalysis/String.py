##### String Formatting #####

## string % tuple formatting --
    ## hashing data type
    ## space formatting ( %10
    ## one-to-one substitution
    ## substitutes in a tuple
format_str="Hello, %s. %s are you?"
values_tp=("world", "How")
print(format_str % values_tp)

format1_str="Pi with three decimals: %.3f"
from math import pi
print(format1_str % pi)

"%s + %s = %s" % (1,1,2)
"Pi as a float: %f..." % pi
s="%10.2f" % pi  n ## space formatting
print(s)

s="Con tu eres?"
print("%.5s" % s)  ## slicing

## "{}".format() --
    ## hashing data type
    ## space formatting
    ## one-to-one substitution
    ## substitutes in a tuple
"{}, hi {}, great {}".format(1,2,3)
"{:=30}, hi {}, great {}".format(1,2,3)
"Pi with three decimals: {:=.3f}".format(pi)

## Template().substitute() --
    ## one-to-many substitution
    ## variable substitution
    ## substitutes in a dictionary
from string import Template
s=Template("$x, hi $x, great $x")
s.substitute(x="Sarah")
s.substitute(x="Noah")

ss=Template("$x and $y sit on the tree")
ss.substitute(x="Sarah", y="Noah")

d={}
d["x"]="Juan"
d["y"]="Matteo"
ss.substitute(d)

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

