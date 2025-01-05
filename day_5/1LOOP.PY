#for___in loop #this loop looks back in the list after printing first value of list it loops back and print back the second value and continues to do so

fruits = ["apple","peach","pear"]
for fruit in fruits:  
    print(fruit)
    print(fruit + " pie")
    print(fruits)
print(fruits) #(this line is outside of loop so it will be printed only once but the above lines which are inside loop will print out every time the loop runs)   
