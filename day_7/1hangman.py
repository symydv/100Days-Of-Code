# for tree chart refer to a image in another file
import random

from hangman_words import logo

from hangman_words import words # it will import the words we have used in the game from another file we have already saved


word = random.choice(words)
# print(word)


lives = 6

display= []
for n in range(0,len(word)):    # or (for n in word:)
    display += "_"
print(display) 


endofgame = False

while not endofgame:    # or (endofgame == false)

    guess = input("guess a letter\n").lower() 

    if guess in display:
        print(f"you've already guessed {guess}")


    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
         display[position] = letter 


    if guess not in word:

        print(f"you guessed {guess}, that's not in word. you loose a life.")

        lives -= 1

        if lives == 0:
            endofgame = True
            print("you loose")  

    print(display)
        

    if "_" not in display:     # here in is used to check the presence of an element in list
            endofgame = True
            print("you win")















