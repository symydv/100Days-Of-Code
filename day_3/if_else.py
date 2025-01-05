#ex 
water_level= 50
if water_level>80:
    print("drain water")
else:
    print("continue")

#this is used a conditional statement.


#project using if else statement (rollercoster height limitter)


print("welcome to the rollercoaster")
height = int(input("what is your height in cm ?"))
if height >= 180:    #(to use strictly equal to 180 or should not be equal to 180 we have to use "==" and "!=" signs)
    print("you can enter")
else:
    print("sorry you cant enter")


# more complex if else func
 
print("welcome to the rollercoaster")
height = int(input("what is your height in cm ?"))
if height >= 180:    #(to use strictly equal to 180 or should not be equal to 180 we have to use "==" and "!=" signs)
    print("you can enter")
    age=int(input("what is your age ?"))
    if age>=18:
     print("please give 18$")
    else:
        print("please give 7$")

else:
    print("sorry you cant enter")




