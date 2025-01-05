#for more complex if else function inside the if else func we use elif function
# we can use as many elif conditions in between if else as many we wants



print("welcome to the rollercoaster")
height = int(input("what is your height in cm ?"))
if height >= 180:    #(to use strictly equal to 180 or should not be equal to 180 we have to use "==" and "!=" signs)
    print("you can enter")
    age=int(input("what is your age ?"))
    if age<12:
       bill=5
       
    elif age<=18:
        bill=7

    else:
        bill=18

    wants_photo=input("do you wants a photo taken ? y or n.")

    if wants_photo=="y":
      bill+=3
      print(f"you have to pay {bill} $")

    else:
        print(f"no problem enjoy the ride and pay {bill}$")

else:
    print("sorry you cant enter")
