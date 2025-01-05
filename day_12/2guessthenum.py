import random

ans = random.randint(1,100)

level = input("choose  level easy with 10 lives or hard with 5 lives: ")

if level == "easy":
    lives = 10
    while lives >= 1 :
        guess = int(input("guess a number between 1 to 100: "))
        if guess == ans:
            print("congrats 🎉 you guessed the number right you won")
            break
        elif guess >= ans:
            lives -= 1
            print(f"too high📈\nlives ramaining:{lives}")
        elif guess <= ans:
            lives -= 1
            print(f"too low📉\nlives remaining:{lives}")
    if lives == 0:
        print(f"you lost all your lives\ncorrect ans was {ans}")


elif level == "hard":
    lives = 5
    while lives >= 1 :
        guess = int(input("guess a number between 1 to 100: "))
        if guess == ans:
            print("congrats 🎉 you guessed the number right you won")
            break
        elif guess >= ans:
            lives -= 1
            print(f"too high📈\nlives ramaining:{lives}")
        elif guess <= ans:
            lives -= 1
            print(f"too low📉\nlives remaining:{lives}")
        
    if lives == 0:
        print(f"you lost all your lives\ncorrect ans was {ans}")



