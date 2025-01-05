print("welcome to love calculator")
name1=input("what is your name?")
name2=input("what is their name?")
# name1=name1.lower()
# name2=name2.lower()
# true=int(name1.count("t") + name2.count("t") +name1.count("r")+name2.count("r")+name1.count("u")+name2.count("u")+name1.count("e")+name2.count("e"))
# love=int(name1.count("l")+name1.count("o")+name1.count("v")+name1.count("e")+name2.count("l")+name2.count("o")+name2.count("v")+name2.count("e"))
# lovescore=int(str(true)+str(love))
# if lovescore<=10 or lovescore>=90:
#     print(f"your love score is {lovescore} you go together like coke and mentos")
# elif lovescore>=40 or lovescore<=50:
#     print(f"your score is {lovescore} you are alright together ")
# else:
#     print(f"your score is {lovescore}")


#-----------OR---------------------------------------------------------------------------------------------------#


name=name1+name2
name=name.lower()
true=int(name.count("t") + name.count("r") + name.count("u") + name.count("e") )
love=int(name.count("l") + name.count("o") + name.count("v") + name.count("e"))

lovescore=int(str(true)+str(love)) 

if lovescore<=10 or lovescore>=90:
    print(f"your love score is {lovescore} you go together like coke and mentos")
elif lovescore>=40 or lovescore<=50:
    print(f"your score is {lovescore} you are alright together ")
else:
    print(f"your score is {lovescore}")
