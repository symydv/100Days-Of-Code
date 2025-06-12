from tkinter import *

window = Tk()
window.title("GUI program")
window.minsize(width=500, height=300)


###############################################################################################
#Lable()
lable = Label(text="my lable", font=("Arial", 15, "bold"))
lable.pack() #the above line wont show on screen without this .pack()
#expand=True get the lable to middle center, side = left will take it to top left
#check documentation for more
lable["text"] = "new text" #it will edit the text provided previosly
#we can also use lable.config(text = "new text")


##################################################################################
#Entry() #to get inputs

input = Entry(width=10) 
input.pack()
print(input.get()) #it returns the input we have given



################################################################################################
#Button()

def button_clicked():
    lable.config(text =input.get())

button = Button(text="click me", command=button_clicked)
button.pack()


################################################################################
#Text()

text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


#############################################################################################
#Spinbox()

def spinbox_used():
    #gets the current value in spinbox.
    text.insert(END,spinbox.get())
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


#########################################################################################
#Scale()

#Called with current scale value.
def scale_used(value):
    text.insert(END,f"{value},")
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


#############################################################################################
#Checkbutton()

def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


############################################################################################
#Radiobutton()

def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

############################################################################################
#Listbox()

def listbox_used(event):
    # Gets current selection from listbox
    text.insert(END,f"{listbox.get(listbox.curselection())},")
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()#should be at the end of code using tkinter



