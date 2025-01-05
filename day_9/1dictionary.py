words = {"hello": "world", "by": "me"}



#to make a dictionary more readable we can make it lilke this
programming_dictionnary = {
    "bug": "an error in a program",
    "function": "in built programes",
    "loop": "doing something over and over agian",
    123: "just some random num"
}



#to call out something from a dict we use below function it is simmilar as lists but we use the inside variable insead of poaition.
print(programming_dictionnary["bug"])





#to add new item to dictionary
programming_dictionnary["haha"] = "by by"
print(programming_dictionnary)





# Edit an item in dictionary
programming_dictionnary["bug"] = "a moth in your computer"
print(programming_dictionnary)






# Loop through a dictionaary
for key in programming_dictionnary:
    print(key) #It will provide you just the key in dict
    print(programming_dictionnary[key]) #it will provide the value inside the dictionary