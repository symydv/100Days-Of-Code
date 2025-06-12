import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

image = "day_25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


#################################################################
#to get the coordinate of states by clicking  on the image use below code
#but we have already got this coor in csv file using this
'''
 def get_mouse_click_coor(x,y):
     print(x,y)

 turtle.onscreenclick(get_mouse_click_coor)
 turtle.mainloop() #to run code even after click

'''
##################################################################



data = pandas.read_csv("day_25/50_states.csv")
x = data.state
state_name = x.to_list()

game_is_on = True
ans_list = []
while game_is_on :
    t = turtle.Turtle()
    t.hideturtle()
    t.up()
    ans_state = screen.textinput(title=f"{len(ans_list)}/50 States correct", prompt="What's another State's name ?").title()

    if ans_state == 'Exit':
        missing_states = [state for state in state_name if state not in ans_list] 
        print(missing_states)         
        break
    if  ans_state in state_name:
        row = data[data.state == ans_state]
        x_coor = int(row.x)
        y_coor = int(row.y)
        t.goto(x_coor,y_coor)
        t.down()
        t.write(ans_state,align = "center", font= ("Courier", 10 ,"normal"))
        ans_list.append(ans_state)

    if len(ans_list)>=50:
        print("you won the game")
        t.goto(0,0)
        t.write("you won the game",align = "center", font= ("Courier", 30 ,"normal"))
        game_is_on = False



 