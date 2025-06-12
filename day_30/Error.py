#FileNotFound error

# with open("./day_30/a_file.txt") as file:
#     file.read()


#KeyError
# a_dict = {"key":"value"}
# value = a_dict["non_existing_key"]

#IndexError
# fruit_list = ["apple", "Banana", "Pear"]
# fruit = fruit_list[3]

#TypeError

# txt = "abc"
# print(txt+5)


# try:
#     file = open("./day30/a_file.txt")
#     a_dict = {"key":"value"}
#     # value = a_dict["non_existing_key"]
#     value = a_dict["key"]
# except FileNotFoundError: #if above file has this error do this
#     file = open("./day_30/a_file.txt", "w") #it will create a new file
#     file.write("something")

# except KeyError as error_message:
#     print(f"The key {error_message} doesnt exist")

# else: #if above all the conditions dont get error then this will happen
#     content = file.read()
#     print(content)

# finally: #this will happen no matter what  happens
#     file.close()
#     print("File was closed")
#     raise KeyError("This is an error that I made up") #we will raise our own error 
    


height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight/height**2
print(bmi)
