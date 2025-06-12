from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizeInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window =  Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score = 0
        self.text = Label(text=f"Score: {self.score}")
        self.text.grid(column=1,row=0)
        self.text.config(bg=THEME_COLOR, foreground="white")

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150,125,width=280,text="some question text",fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(column=0,row=1,columnspan=2)

        right_image = PhotoImage(file="day_34/images/true.png")
        wrong_image = PhotoImage(file="day_34/images/false.png")
        
        self.true = Button(image=right_image, highlightthickness=0,command=self.correct)
        self.true.grid(column=0,row=2)

        self.false = Button(image=wrong_image, highlightthickness=0,command=self.wrong)
        self.false.grid(column=1,row=2)

        self.get_next_que()

        self.window.mainloop()

    def get_next_que(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text )

        else:
            self.canvas.itemconfig(self.question_text, text ="you have reached the end of questions")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def correct(self):
        is_right = self.quiz.check_answer(user_answer="true")
        self.give_feedback(is_right)

    def wrong(self):
        is_right = self.quiz.check_answer(user_answer="false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.get_next_que)






