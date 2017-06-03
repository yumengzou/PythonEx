'''
Created on Jun 3, 2017

@author: yumeng.zou
'''
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
s="%10.2f" % pi    ## space formatting
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
print s.substitute(x="Sarah")
print s.substitute(x="Noah")

ss=Template("$x and $y sit on the tree")
print ss.substitute(x="Sarah", y="Noah")

d={}
d["x"]="Juan"
d["y"]="Matteo"
print ss.substitute(d)