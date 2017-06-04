'''
Created on Jun 3, 2017

@author: yumeng.zou
'''

## Superclass
## inherit methods from the superclass by class_name(superclass)
class Filter():
    def init(self):
        self.blocked=[]
    def filter(self,seq):
        return [i for i in seq if i not in self.blocked]
class SPAMFilter(Filter):
    def init(self):
        self.blocked=["SPAM"]

f0=Filter()
f0.init()
print f0.filter(["apple","SPAM","egg","tomato"])

s=SPAMFilter()
s.init()
print s.filter(["apple","SPAM","egg","tomato"])

print issubclass(SPAMFilter,Filter)
print SPAMFilter.__bases__
print isinstance(s,SPAMFilter)
print isinstance(s, Filter)
print s.__class__, "\n"


## Multiple Superclasses
class calculator():
    def calculate(self,expression):
        self.value=eval(expression)
class talker():
    def talk(self):
        print "My value is ", self.value
class TalkingCalculator(calculator,talker):
    pass

tc=TalkingCalculator()
tc.calculate("1+3/2.0")
tc.talk()


## Interface: the methods and attributes known to the world
print hasattr(tc, "talk")
print hasattr(tc, "filter")
setattr(tc, "name", "Texas")
print tc.name