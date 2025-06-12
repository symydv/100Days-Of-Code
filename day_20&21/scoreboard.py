from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("day_20&21/highScore.txt","r") as data:
            self.HS = int(data.read())
        self.color("white")
        self.up()
        self.goto(-100,270)
        self.write(f"score : {self.score}", align = "center", font= ("Courier", 20 ,"normal"))
        self.hideturtle() #used to hide the arrow
        
    def point(self):
        self.score +=1
        if self.score > self.HS:
            self.HS = self.score
        with open("day_20&21/highScore.txt", mode="w") as data:
            data.write(f"{self.HS}")

        self.clear()
        self.goto(-100,270)
        self.write(f"score : {self.score}", align = "center", font= ("Courier", 20 ,"normal"))
        self.highScore()

    def game_over(self):
        self.score = 0
        self.goto(0,0)
        self.write(f"GAME OVER", align = "center", font= ("Courier", 20 ,"normal"))
        
        
        
    def highScore(self):
        self.goto(100,270)
        self.write(f"H.S. : {self.HS}", align = "center", font= ("Courier", 20 ,"normal"))
       
   