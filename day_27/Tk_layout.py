from tkinter import *

window = Tk()
window.title("GUI program")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20) #add padding(space around programme)

lable = Label(text="my lable", font=("Arial", 15, "bold"))
# lable.place(x=100,y=100) #place is used for precise positioning
lable.grid(column=0,row=0) #also used for precise positioning
#first item using grid will be relative for all other items.
#so even if you change column=0,row=0 to something else its position wont change
#cant use grid() and pack in same code
lable["text"] = "new text" 
lable.config(padx=20,pady=20)

button = Button(text="click me")
button.grid(column=1,row=1)

#Entry()
input = Entry(width=10) 
input.grid(column=3,row=2)
print(input.get())


new_botton = Button(text= "new button")
new_botton.grid(column=2,row=0)

window.mainloop()