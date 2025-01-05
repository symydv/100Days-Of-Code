print(round(8/3)) #use round function for rounding of we can also use int function but it will conver 2.6 into 2 not round it off to 3 
print(round(8/3,2))# using ",2" round off off the value upto 2 decimal palces
print(8//3)#also gives result as an int function if you check the data type of this it will show you int





result=4/2
result/=2 #(this is like writing result=result/2) we can also  use result+=1 instead of result = result + 1 and many more functions)
print(result)



# f-string
score=0
height=1.8
iswinning=True

print(f"your score is {score}, your height is  {height} ,you are winning is {iswinning}") # here if we have to  write score after your score is we would have to first convert given score variable which currently is an int into a string but for many values it is very hard to add str function in every given data so we can just add f befoe "__" and the given values which ve have to make strings into{} to get the required ans
