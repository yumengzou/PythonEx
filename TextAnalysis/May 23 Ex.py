print("Hello, World!")
## in Python 3, print("String")

##### Data Type #####
1/2
## 0.5
## in Python 3, the quotient of two intergers can be a float
## if you want integer, use int(1/2) or round(1/2)

##### User Input #####
s = input("x: ")
## prompt the user for imput, input is a string
pow(2,3)
## equivalent to 2**3 = 8

##### Modules #####
import math
math.floor(2/3)
## equivalent to round
math.sqrt(9)
## equivalent to 3**(1/2)
import cmath
cmath.sqrt(-1)
## 1j

##### String #####
"Let's go"
## equivalent to 'Let\'s go'
x="Hello"
y="World"
z=42
x+y+repr(z)
x+y+str(z)
repr(x) returns a string that Python can understand
str(x) returns a string that user can understand

s='''This is a long string
that can be followed by multiple lines
and it starts with three quote marks'''
## >>> s
## 'This is a long string\nthat can be followed by multiple lines\nand it starts with three quote marks'
s2="This is a long string\
that can be followed by multiple lines\
and it needs slash after each line"
## >>> s2
## 'This is a long stringthat can be followed by multiple linesand it needs slash after each line'

##### Function #####
def mymulti(x,y):
	ans=0
	for i in range(x):
		ans=ans+y
	return ans
mymulti(9,5)
