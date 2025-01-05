import random

computer_choice = ["rock","paper","scisor"]
computer_choice = random.choice(computer_choice)

my_choice = int(input("choose 1 for rock , 2 for paper and 3 for scisor: "))


if my_choice == 1:
    
    print(f"you choose rock \ncomputer choose {computer_choice}")
    if computer_choice=="rock":
        print("its a draw") 
    elif computer_choice=="scisor":
        print("you won")    
    else :
        print("you loss!") 





if my_choice == 2:
    print(f"you choose paper \ncomputer choose {computer_choice}")
    if computer_choice=="paper":
        print("its a draw") 
    elif computer_choice=="rock":
        print("you won")    
    else :
        print("you loss!") 




if my_choice == 3:
    print(f"you choose scisor \ncomputer choose {computer_choice}")
    if computer_choice=="scisor":
        print("its a draw") 
    elif computer_choice=="paper":
        print("you won")    
    else :
        print("you loss!")      