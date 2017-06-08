##### Dictionary #####

def contact():
	contact={}
	while True:
		name=input("What's your name? ")
		if name=="":
			break
		phone=input("What's your phone number? ")
		address=input("What's your address? ")
		contact[name]=dict(phone=phone,address=address)
	return contact

mycontact=contact()

y=mycontact.copy()

y["Sarah"]["phone"]=15801142172
y
mycontact ## mycontact changes with y

y["Noah"]="NaN"
y
mycontact ## mycontact doesn't change

list(y.keys())
sorted(y.keys())

x={}.fromkeys("test1","test2")
x         ## {'t': 'test2', 'e': 'test2', 's': 'test2', '1': 'test2'}
x={}.fromkeys(["test1","test2"])
x         ## {'test1': None, 'test2': None}
