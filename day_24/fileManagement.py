''' Using file management we can creatae a global high score 
in our snake game which will not even be deleted 
after closing and reopening the game'''



file = open("day_24/my_file.txt")
y = file.read()
print(y)
file.close() 

# IN above code we have to close the file manually
#but by using "with" the file automatically closes after the use

# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)

with open("day_24/my_file.txt",mode="w") as file: #changed mode from read only to write
    file.write("New text.")                                       


''' But "w" mode will delete the previous content to 
be able to just add another text without deleting previos text
we can use "a"  mode'''
    

with open("day_24/my_file.txt",mode="a") as file: 
    file.write("\nAnother new text.")


#if a file doesnt exist it will create a new one for you

with open("day_24/new_file.txt",mode="a") as file: 
    file.write("New_file.")

