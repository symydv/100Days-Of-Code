# we can store many data in only one variable together through lists
#obj inside lists are saperated by commas and all are contained in square bracket


states=["madhya pradesh" , "up", "gujrat"]

print(states[0]) #programming counting starts from 0

print(states[-1]) # negative number starts counting from backwards, last word is -1

states[2]="maharashtra" # this is to edit the list content
print(states)


states.append("jharkhand") # used to add more data at the end of the list
print(states)

# there are many more function that can be used int he lists so just google them and learn about them

states.extend(["haryana","rajasthan","kerela"]) #adds many datas at the end 
print(states)
states.insert(3,"punjab") #inserted punjab at 4th position
print(states)

states.pop(2) #to remove the 3rd entry in list
print(states)

states.clear() # to clear the list
print(states)
