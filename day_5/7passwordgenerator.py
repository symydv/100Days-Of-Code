
import random

latters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


print("welcome to the password generator!")


nr_letters = int(input("how many letters would you like in your password?\n"))
nr_numbers = int(input("how many numbers do you want in you password ?\n"))
nr_symbols = int(input("how many symbols do you want in you password ?\n"))

# easy level (here letters are together then numbers are together theen symbols are together)

password = ""

for n in range(0,nr_letters): #(to get a loop nr_letters time)
    random_letter = random.choice(latters) #(it will choose a letter in every round of loop)
    password += random_letter #(add one letter to password in every round of loop)


for m in range(0,nr_numbers):
    random_num = random.choice(numbers)
    password += random_num
  

for p in range(0,nr_symbols): #(we could also take (1,nr_symbols+1))
    random_symbol = random.choice(symbols)
    password += random_symbol
   

print(f"your password is :{password}")


#-------hard level (completely random position of numbers , letters and symnbols)--------



password_list = [] #(this time we will creat a list first)

for n in range(0,nr_letters): 
    random_letter = random.choice(latters)
    password_list += random_letter  #(we can also you .append() to add an item to the list and also use the same function we are using here)


for m in range(0,nr_numbers):
    random_num = random.choice(numbers)
    password_list += random_num
  

for p in range(0,nr_symbols): 
    random_symbol = random.choice(symbols)
    password_list += random_symbol
#(now to randomise the content of the list we can use shuffle function )



random.shuffle(password_list)
 #(now turn that list back into the string)


password = ""
for character in password_list:
    password += character


print(f"your password is: {password}")