#unlimited argument function

def add(*arg): #using "*arg" (can use any name instead of arg) func can get unlimited arguments
    total = 0
    for n in arg:
        total += n
    print(total)

add(1,2,3,4)

#############################################################################
def calculate(n,**kwarg):# "**" are used for keyword arguments
    # print(kwarg)
    # for key, value in kwarg.items():
    #     print(key)
    #     print(value)

    n += kwarg["add"]
    n *= kwarg["multiply"]
    print(n)

calculate(2,add=3, multiply=5)#this will return a dictionary{"add":3, "multipy":5}

#############################################################################


class car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.gwt("seats")
        

mycar = car( model="GT-R")
print(mycar.make)
'''notice we didnt provided key word make in use 
of function but it will not show error becouse
we are using .get() it will just print none.
if we have directly used kw["make"] 
it would have showed error while running
'''



