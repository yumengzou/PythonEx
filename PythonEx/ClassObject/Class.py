'''
Created on Jun 3, 2017

@author: yumeng.zou
'''

## must write this before creating class
from bs4.tests.test_docs import __metaclass__
__metaclass__=type

## self=this
## don't need to initialize instance variables outside of methods
class Person():
    
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def greet(self):
        print "Hello World! I'm %s" % self.name
    
p1=Person()
p2=Person()
p1.setName("Sarah")
p2.setName("Noah")
p1.greet()
p2.greet()

print "{:20}{:10} = {}".format("method","getName()", p1.getName())
print "{:20}{:10} = {}\n".format("instance variable",".name",p2.name)

## "__" will make a method private
## which means can not be accessed by the user
## but only by other methods within the class
class Secretive():
    def __inaccessible(self):
        print "This message can only by used within the class"
    def accessible(self):
        print "The secret message is: ", self.__inaccessible()

s=Secretive()
## s.__inaccessible()
s.accessible()
s._Secretive__inaccessible()
print

## a class variable can be accessed and changed by all instances in the class
## both instance variables and class variables are class attributes
## self.var is instance variable; class.var is class variable
class MemberCounter():
    members=0
    def init(self):
        MemberCounter.members+=1

m1=MemberCounter()
m1.init()
print "{:30} = {}".format("MemberCounter.members", MemberCounter.members)

m2=MemberCounter()
m2.init()
print "{:30} = {}".format("after creating m2", MemberCounter.members)

print "{:15} = {}".format("m1.members",m1.members)
print "{:15} = {}".format("m1.members",m1.members)
print "class variable can be accessed by all instances"

## Assigning a new value as an instance variable to m1
m1.members="Two"
print "Assigning a new value as an instance variable to m1, \
\nm1.members = {}; m2.members = {}".format(m1.members, m2.members)

