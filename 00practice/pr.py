#avg of the given numbers 

numbers=input("enternumbers you want to fin average of\n")
numbers=numbers.split(",")
sum=0
for n in numbers:
    sum+=int(n)
x=len(numbers)

avg=sum/x
print("the avg number is: ",avg)