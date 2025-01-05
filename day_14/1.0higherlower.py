######MY CODE########################
import random 
import os
from gamedata import data
from art import logo 
from art import vs
score = 0
lost = False

def check_ans():
    global lost
    global score
    if guess == "a" :
        if a_followers>b_followers:
            os.system("cls")
            print("correct ans 😊")
            score += 1
        elif b_followers>a_followers:
            lost = True
            score = score

    elif guess == "b" :
        if a_followers<b_followers:
            os.system("cls")
            print("correct ans 😊")
            score += 1
        elif b_followers<a_followers:
            lost = True
            score = score


choice_a = random.choice(data)
while lost == False:

    print(logo)



    print(f"compare A: {choice_a["name"]}, a {choice_a["description"]} from {choice_a["country"]}")

    a_followers = choice_a["follower_count"]
    
    print(vs)

    choice_b = random.choice(data)
    if choice_a == choice_b:
        choice_b = random.choice(data)

    print(f"against B: {choice_b["name"]}, a {choice_b["description"]} from {choice_b["country"]}")

    b_followers = choice_b["follower_count"]
    
    guess = input("which of them have more followers on insta option a or b: ").lower()
    check_ans()
    choice_a = choice_b
    if lost == True:
        break
    
    print(f"current score: {score}")

os.system("cls")
print("sorry incorrect ans 😔")
print(f"final score: {score}")



#########MAAM"S CODE###########################
#on another page named maamscode.py
#and definately check  replit for this code to read the details



