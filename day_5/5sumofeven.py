# to get the sum of even numbers from 1 to 100 including 100


sum=0
for num in range(1,101):
    if num%2 == 0:
        sum += num
print(sum)        



#--------OR-------------------
sum=0
for num in range(2,101,2):
    sum += num
print(sum)   
