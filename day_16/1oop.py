#class is a large term we can create many objects from a class like many cars can be created fromm one blueprint
#object- the car in above line which we have created from a class
#they generaly look like--
# object = class() #we can import larger classes also called libraries eg.- turtle

#attributes(thing an obj holds)
#data stored inside objects 
#denoted as--
#car.speed (here car is obj and speed is one of its attributes and they are separated by a comma)



#object methods(things an obj can do)
#denoted as--
#car.stop()  #here stop() is a method which we have to define or it is contaoned in the library we have imported


from turtle import Turtle,Screen
timmy = Turtle()
raju = Screen()
print(timmy)

timmy.shape("turtle")
timmy.color("coral")
timmy.speed(0)
x=0
y=100
while x<=100:
    
    timmy.forward(100)
    timmy.left(y)
    timmy.forward(100)
    timmy.left(y)
    timmy.forward(100)
    y+=1
    x+=1
myscreen = Screen()
print(myscreen.canvheight)
myscreen.exitonclick()

#go on python package index to find more packeges like turtle and know how to use them

# from prettytable import PrettyTable
# table= PrettyTable()
# table.add_column("pokemon name",["pikachu","squirtle","charmender"])
# table.add_column("type",["electric","water","fire"])
# table.align="l"  #(it aligns the characters in column to left, here align is an attribute and add_column is a method)

# print(table)