'''
Created on Jun 3, 2017

@author: yumeng.zou
'''
##### Dictionary #####

def contact():
    contact={}
    while True:
        name=raw_input("What's your name? ")
        if name=="":
            break
        phone=raw_input("What's your phone number? ")
        address=raw_input("What's your address? ")
        contact[name]=dict(phone=phone,address=address)
    return contact

mycontact=contact()
print mycontact
y=mycontact.copy()

y["Sarah"]["phone"]=15801142172
print y
print mycontact ## mycontact changes with y

y["Noah"]="NaN"
print y
print mycontact ## mycontact doesn't change

print list(y.keys())
print sorted(y.keys())

x1={}.fromkeys("test1","test2")
print x1        ## {'t': 'test2', 'e': 'test2', 's': 'test2', '1': 'test2'}
x2={}.fromkeys(["test1","test2"])
print x2         ## {'test1': None, 'test2': None}
