from tkinter import *
from pandas import *
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = read_csv("day_31/Words_to_learn.csv")
except FileNotFoundError:
    data = read_csv("day_31/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")  #it creates a list of dictionaries


def next_card():
    global current_card,flip_timer
    windows.after_cancel(flip_timer) #it cancels any ongoing timers, if we dont do that our timer of 3 sec will flip the card even if wwe changed to another card.
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text= "French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background,image=front_image)
    flip_timer = windows.after(3000, func=flip_card)
    
def flip_card():
    canvas.itemconfig(title, text =  "English",fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill = "white" )
    canvas.itemconfig(card_background, image=back_image)

def is_known():
    to_learn.remove(current_card)
    data= DataFrame(to_learn)
    data.to_csv("day_31/Words_to_learn.csv",index=False)
    next_card()

###################################################################################
windows = Tk()
windows.title("Flashy")

windows.config(padx=50,pady=50,background=BACKGROUND_COLOR)

flip_timer = windows.after(3000, func=flip_card)

front_image = PhotoImage(file="day_31/images/card_front.png")
back_image = PhotoImage(file="day_31/images/card_back.png")
cross_image = PhotoImage(file="day_31/images/wrong.png")
check_image = PhotoImage(file = "day_31/images/right.png")


canvas = Canvas(width=800, height=526)

canvas.create_image(400, 263, image= front_image)
card_background = canvas.create_image(400,263,image = front_image)
word = canvas.create_text(400,263,text="Word",font=("Ariel", 60, "bold"))
title = canvas.create_text(400,150,text="Title",font=("Ariel", 60, "italic"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

unknown_button = Button(image=cross_image, highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)

known_button = Button(image=check_image, highlightthickness=0,command=is_known)
known_button.grid(row=1,column=1)

next_card()
######################################################################################################


windows.mainloop()