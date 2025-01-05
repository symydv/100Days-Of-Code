def greet_with(name,location): # mare than one parameter as input
    print(f"hello {name}")
    print(f"I got to know that you shifted to {location} last week")

greet_with("shivam","Alaska")  #(position argument)  

greet_with(location="Alaska", name="shivam") #(keyword argument)