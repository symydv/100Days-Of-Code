from question import Question

class QuizBrain:
    def __init__(self,q_list):
        self.que_list = q_list
        self.que_no = 0
        self.score = 0

    def next_que(self):
        current_que = self.que_list[self.que_no]
        self.que_no += 1
        user_ans = input(f"Q.{self.que_no}: {current_que.text} (True/False) : ")
        self.check_ans(user_ans, current_que.ans)
    def stillhasQue(self):
        if self.que_no<len(self.que_list):
            return True
        else:
            return False
        
    def check_ans(self, user_ans, correct_ans):
        if user_ans == correct_ans.lower():
            print("you got it right! ")
            self.score += 1
            print(f"your current score is : {self.score}/{self.que_no}")
        else:
            print("you got it wrong. ")
            print(f"your current score is : {self.score}/{self.que_no}")
            


Question_data = [
    {"text": "A slug's blood is green.", "answere": "True"},
    {"text": "The loudest animal is African Eliphant.", "answere": "false"},
    {"text": "The surface area of human lungs is size of footvball field.", "answere": "False"},
    {"text": "Its illegal to pee in ocean in Portugal.", "answere": "True"},
    {"text": "You can lead a cow down the stair but not up the stairs.", "answere": "False"},
    {"text": "Google was originally called 'Backrub'.", "answere": "True"},
    {"text": "No piece of square paper can be folded  in half more than 7 times.", "answere": "False"},
]

question_bank = []

for x in Question_data:
    que_text = x["text"]
    que_ans = x["answere"]

    new_ques= Question(que_text, que_ans)
    question_bank.append(new_ques)


quiz = QuizBrain(question_bank)
while quiz.stillhasQue():
    quiz.next_que()
    
