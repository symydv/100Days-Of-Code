# we use list comprehension to use methods on list that makes our code shorter
#also works for string

list = [1,2,3,4]
new_list = [n+1 for n in list]
print(new_list)

''' the above code is short cut to create a new_list with help of
existing list whose all elemnts are +1 to same index of list'''


name = "shyam"
letters_list = [letters for letters in name]
print(letters_list)



double = [num*2 for num in range(1,5)]
print(double)


# we can also add conditons using comprehension

names = ["shyam", "anuj", "bhanu", "raj" ,"nikhil"]

short_names = [name for name in names if len(name) < 5]
print(short_names)

big_names = [name.upper() for name in names if len(name) > 4]
print(big_names)

##########
num = [1,1,2,3,5,8,13,21,34,55]
square = [number*number for number in num]
print(square)

even = [number for number in num if number%2==0]
print(even)


##########
file1 = open("day_26/list1.txt",'r')
f1 = file1.readlines()
file2 = open("day_26/list2.txt",'r')
f2 = file2.readlines()

same = [int(l1) for l1 in f1 if l1 in f2]


print(same)