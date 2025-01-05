# '''path is complete path of a file 
#  eg: E:\code\python\ 100 days Code\day_24\ filepath.py  
#  this is the path of current file
# '''

# """directory is relative path of a folder means
# if we want to get hold of a file in same 
# folder as our current file 
# we can use the ./fileManagement.py 
# or day_24\ fileManagement.py  "." is used here"""



#in below example we have used absolute path to access a file out of this folder
#we can directly copy the path and use or can use such type used below
# we can use "/" or "\" python dont care

#in below example we have used absolute path to access a file out of this folder

with open("/code/python/shyam.txt") as file:
    content = file.read()
    print(content)


#now using relative path
#so from our folder to go to python folder 
#we need to go two level up so for one level we use "../"
#for two level we use "../../"

with open("../../python/shyam.txt") as file2:
    data = file2.read()
    print(data)