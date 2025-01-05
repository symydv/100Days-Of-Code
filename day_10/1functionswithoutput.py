# functions with output 

def format_name(f_name, l_name):
    formated_f = f_name.title() #.title() is used to convert first letter capital and others small
    formated_l = l_name.title()
    return f"{formated_f} {formated_l}" #it replaces the defined function where ever it is called with the output in the return function you can thinkn it works as print function
    
print(format_name("angEla", "AnGElA"))



# Multiple return kvalues

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "you didn't provided valid inputs."
    formated_f = f_name.title() 
    formated_l = l_name.title()
    return f"Result: {formated_f} {formated_l}"
    
print(format_name(input("what is your first name:"), input("what is your last name?:")))


