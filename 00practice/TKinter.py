from tkinter import *

tk = Tk()
tk.title("my APP")
tk.minsize(width=400, height=600)

lable = Label(text="my profile", font=("Arial", 15, "bold"))
lable.place(relx = 0.0,rely = 0.0,anchor ='nw')

Label1 = Label(text="Followers", font=("Arial", 10, "bold"))
Label1.place(relx = 0.45,rely = 0.0)

Label2 = Label(text="Following", font=("Arial", 10, "bold"))
Label2.place(relx = 0.65,rely = 0.0)


x =0
Label12 = Label(text=f"{x}", font=("Arial", 10, "bold"))
Label12.place(relx = 0.45,rely = 0.05)
Label22 = Label(text="0", font=("Arial", 10, "bold"))
Label22.place(relx = 0.65,rely = 0.05)




def followed():
    global x
    x+=1
    Label12.config(text= x)

button = Button(text="FOLLOW",command=followed)
button.place(relx=0.45,rely=0.1)


tk.mainloop()