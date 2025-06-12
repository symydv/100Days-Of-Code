from tkinter import *

window = Tk()
window.title("Miles to Km converter")
window.config(padx=20,pady=20)


miles = Entry(width=10)
miles.grid(column=1,row=0)
x=Label(text="Miles",font=(1))
x.grid(column=2,row=0)

z=Label(text="is equal to",font=(1))
z.grid(column=0,row=1)

Km = Label(width=10,font=(1))
Km.grid(column=1,row=1)
y=Label(text="Km",font=(1))
y.grid(column=2,row=1)

def miles_to_km():
    Km.config(text = round(float(miles.get())*1.609,3))


calc = Button(text="Calculate",command=miles_to_km)
calc.grid(column=1,row=2)




window.mainloop()