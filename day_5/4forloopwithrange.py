# for loop with Range

for number in range(1,10): # 1 to 10 excluding 10, to get 1 to 10 including 10 write range(1,11)
    print(number)






#to make it take steps and leap some numbers we have to add how many numbers we want to leap at last 
for number in range(1,11,3): # it will leap to third word from previos one
    print(number)    





# to get sum of all the numbers from 1 to 100
total = 0
for num in range (1,101):
    total += num
print(total)    