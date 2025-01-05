import random
import os
# apne code ko thoda sahi kar bhai
cards = [11, 2, 3 , 4 ,5, 6, 7, 8, 9, 10, 10, 10, 10]

    

user_cards = []
comp_cards = []

#======ye wala mene banaya hai jisme admi sirf baith kar dekhta hai use kuch nhi karna padta[mtlb faltu banaya hai]======

# game_finish = False

# while game_finish == False:
#     user_cards.extend([random.choice(cards), random.choice(cards)])
#     comp_cards.extend([random.choice(cards), random.choice(cards)]) 

#     print(f"your cards are {user_cards}")
#     print(f"computer cards are{comp_cards}")


#     sum_user = int(user_cards[0] + user_cards[1])
#     sum_comp = int(comp_cards[0] + comp_cards[1])


#     if sum_user>21 and sum_comp<=21 :
#         print("you loose because sum of your cards is more than 21")

#     elif sum_comp>21 and sum_user<=21 :
#         print("you won as sum of computers cards are more than 21")

#     elif sum_user>21 and sum_comp>21 :
#         print("both have card sum more than 21 its a draw")

#     else:
#         if sum_user<17 and sum_comp>=17 :
#             user_cards.append(random.choice(cards))
#             print("your cards sum is less than 17 so we have added one extra card")
#             print(f"now your cards are {user_cards}")
#             sum_user = int(user_cards[0] + user_cards[1] + user_cards[2])
#         elif sum_comp<17 and sum_user>=17 :
#             comp_cards.append(random.choice(cards))
#             print("comp card sum is less than 17 so we have added extra card to it")
#             print(f"now comp cards are {comp_cards}")
#             sum_comp = int(comp_cards[0] + comp_cards[1] + comp_cards[2])
#         elif sum_user<17 and sum_comp<17 :
#             user_cards.append(random.choice(cards))
#             comp_cards.append(random.choice(cards))
#             print("both your and comp card sum is less than 17 so we added cards to both of them")
#             print(f"your cards are: {user_cards} and comp cards: {comp_cards}")
#             sum_comp = int(comp_cards[0] + comp_cards[1] + comp_cards[2])
#             sum_user = int(user_cards[0] + user_cards[1] + user_cards[2])
#         else:
#             x = input("do you want to add another card or not type 'y' if yes or type 'n' for no\n")
#             if x == "y":
#                 user_cards.append(random.choice(cards))
#                 print(f"now your cards are: {user_cards}")
#                 sum_user = int(user_cards[0] + user_cards[1] + user_cards[2])
        

#         if sum_user>21 and sum_comp<=21 :
#             print("you loose because sum of your cards is more than 21")

#         elif sum_comp>21 and sum_user<=21 :
#             print("you won as sum of computers cards are more than 21")

#         elif sum_user>21 and sum_comp>21 :
#             print("both have card sum more than 21 its a draw")

#     if sum_user>sum_comp and sum_user<=21:
#         print(f"your cards sum is {sum_user} which is more than comp sum:{sum_comp} so you won")
#     elif sum_user<sum_comp and sum_comp<=21:
#         print(f"your cards sum is {sum_user} which is less than comp sum:{sum_comp} so you loose")

#     x = input("do you want to continue the game type yes or no\n")
#     if x== "no":
#         game_finish = True
#     else:
#         game_finish = False
#         user_cards.clear()
#         comp_cards.clear()
#         os.system("cls")


#-------OR--------by maam
        
def deal_card():
    cards = [11, 2, 3 , 4 ,5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

for _ in range(2):
    new_card = deal_card()
    user_cards.append(new_card)

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""

  #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():

  #Hint 5: Deal the user and computer 2 cards each using deal_card()
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

  while not is_game_over:
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  os.system("cls")
  play_game()






