###########scope############

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


#==local scope==
def drink_potion():
    potion_strength = 2 
    print(potion_strength)

drink_potion()
# print(potion_strength)===its invalid
#here potion_strength is a local scope as we have defined it inside a function we cant use it outside unless we define it outside



#===Globsl scope=====#
player_potion = 10  #This is a global scope as we can now use it anywhere in our function below where it is defined

def something():
    certain = 2
    print(player_potion)

something()



#====there is no block scope in python eg below

if 3>2:
    my_name = 2 #means inside if statement or while and for loop, defined functions are also global scope whereever the statement is true 

print(my_name)

#=====Modifying Global Scope

enemies = 1

def increase_enemies():
    global enemies   #without using this global function we cannot modify our variable inside function with respect to out side function or else we have to first define our variable inside the function first try it yourself if you cant understsnd . But should not prefer using it because it can cause kathinai and make your code hard to debug
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


#below mwthod is rather easiesr than the previous one

enemies = 1
def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1
enemies = increase_enemies()
print(f"enemies outside function: {enemies}")


#run and check all the codes thoroughly

