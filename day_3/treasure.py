print("welcome to the treasure island ")
print("your mission is to find the treasure ")
way=input("choose a direction to go left or right\n").lower()
if way=='right':
    print("you are killed by a man eating lion you are dead")
elif way=="left":
    medium=input("there is an island visible to reach it by swimming type swim for boat type boat\n")
    if medium=="swim":
        print("your got eaten by a shark you are dead")
    elif medium=="boat":
        door=input("you reached to the island choose a door from red blue or green to get treasure\n")
        if door=="red":
            print("congrates you won the treasure !")
        else:
            print("game over, you are dead!")
else:
    print("invalid option")