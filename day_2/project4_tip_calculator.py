print("welcome to tip calculator")
x=input("what was the total bill?\n")
y=input("what percent tip would you like to give? 10, 12, or 15\n")
z=int(x)*int(y)/100
z+=int(x)
p=int(input("how many people you want to split bill in ?\n "))
bill=round(z/p,2)
#python dont get zero in round func if it comes at last so to get zero we can use final value = "{:.2}".formate(bill) and then  print the final value.
print(f"each person should pay:{bill}")


