from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None
mark = ""
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    global reps

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    label.config(text="Timer",fg=GREEN)
    check.config(text="")
    reps = 1
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global label

    work_sec = WORK_MIN*60
    SHORT_BREAK_sec = SHORT_BREAK_MIN*60
    LONG_BREAK_sec = LONG_BREAK_MIN*60
    if reps%8 == 0:
        label.config(text="Break", fg = RED)
        countDown(LONG_BREAK_sec)
        reps +=1

    elif reps%2 == 0:
        label.config(text="Break", fg = PINK)
        countDown(SHORT_BREAK_sec)
        reps +=1

    else:
        label.config(text="Work", fg = GREEN)
        countDown(work_sec)
        reps +=1



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countDown(count):
    global check
    global timer
    global mark

    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec =f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count>0:
        timer = window.after(1000, countDown, count-1) #it will do something after some time in this case 1000 mS or 1 sec
    else:
        start_timer()
        
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✓"
        check.config(text = mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./day_28/tomato.png")
canvas.create_image(100, 112, image= tomato_img)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))  


canvas.grid(column=1, row=1)  

label = Label(text="Timer", fg = GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
label.grid(column=1, row=0)

start = Button(text="Start", command=start_timer)
start.grid(column=0,row=2)

Reset = Button(text="Reset", command=reset_timer)
Reset.grid(column=2,row=2)

check = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME,11, "bold"))
check.grid(column=1,row=3)

window.mainloop()