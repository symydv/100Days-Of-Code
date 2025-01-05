from turtle import Turtle,Screen
import random

s=Screen()
s.setup(width=900, height=600)
user_bet = s.textinput(title="make your bet", prompt="which turtle will win the race")
print(user_bet)

red = Turtle()
red.color("red")
green = Turtle()
green.color("green")
pink = Turtle()
pink.color("pink")
blue = Turtle()
blue.color("blue")
purple = Turtle()
purple.color("purple")


t=[red,green,pink,blue,purple]
for obj in t:
    obj.shape("turtle")
    obj.pencolor("white")

x=-400
y=-200
for z in t:
    z.up()
    z.goto(x,y)
    z.down()
    y+=100

def move():
    end=False
    while end==False:
        for d in t:
            if d.xcor()>430: #because the screen corner in x=250 and turtle rakes space of 40 pixels so we decreased 40/2 from 250 as end line
                winning_color = d.fillcolor()
                if user_bet == winning_color:
                    print(f"you guessed it right {winning_color} is winner")
                    s.title(f"you guessed it right {winning_color} is winner")
                else:
                    print(f"you guessed it wrong {winning_color} is winner")
                    s.title(f"you guessed it wrong {winning_color} is winner")
                end=True

        r=random.randint(0,10)
        g=random.randint(0,10)
        b=random.randint(0,10)
        pi=random.randint(0,10)
        pu=random.randint(0,10)
        red.forward(r)
        green.forward(g)
        blue.forward(b)
        pink.forward(pi)
        purple.forward(pu)

move()


s.exitonclick()