import random

names=input("give me everybody's name saperated by comma's\n")

names=names.split(",") #this splits every entries we write before and after comma and make a list of it

num_items = len(names)

random_choice = random.randint(0, num_items-1) #we used num_item-1 because we count from 0

who_will_pay = names[random_choice]

print(f"{who_will_pay} will be paying bill")



#or else we could use choice function (we used above function to do it without using the choice function)

import random

names=input("give me everybody's name saperated by comma's\n")

names=names.split(",")
 
billpayer = random.choice(names)
 
print(billpayer)