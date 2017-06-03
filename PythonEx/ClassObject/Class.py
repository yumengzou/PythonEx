'''
Created on Jun 3, 2017

@author: yumeng.zou
'''
from bs4.tests.test_docs import __metaclass__
__metaclass__=type

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

print "{:10} {}".format("getName()", p1.getName())
print "{:10} {}".format(".name",p2.name)


class Secretive():
    def __inaccessible(self):
        print "This message can only by used within the class"
    def accessible(self):
        print "The secret message is: ", self.__inaccessible()

s=Secretive()
## s.__inaccessible()
s.accessible()
s._Secretive__inaccessible()



