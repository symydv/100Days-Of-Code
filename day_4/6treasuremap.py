
# row1 = ["⬜","⬜","⬜"]
# row2 = ["⬜","⬜","⬜"]
# row3 = ["⬜","⬜","⬜"]

# map = [row1,row2,row3]

# print(f"{row1}\n{row2}\n{row3}")

# position = input("where do you want to put your treasure?  ")

# if position[1]=="1":
#     if position[0]=="1":
#         row1[0]=["x"]
#         print(f"{row1}\n{row2}\n{row3}")
#     elif position[0]=="2":
#         row1[1]=["x"]   
#         print(f"{row1}\n{row2}\n{row3}")
#     else:
#         row1[2]=["x"]
#         print(f"{row1}\n{row2}\n{row3}")
# elif  position[1]=="2":
#     if position[0]=="1":
#         row2[0]=["x"]
#         print(f"{row1}\n{row2}\n{row3}")
#     elif position[0]=="2":
#         row2[1]=["x"]   
#         print(f"{row1}\n{row2}\n{row3}")
#     else:
#         row2[2]=["x"]
#         print(f"{row1}\n{row2}\n{row3}")      
# elif position[1]=="3":
#     if position[0]=="1":
#         row3[0]=["x"]
#         print(f"{row1}\n{row2}\n{row3}")
#     elif position[0]=="2":
#         row3[1]=["x"]   
#         print(f"{row1}\n{row2}\n{row3}")
#     else:
#         row3[2]=["x"]
#         print(f"{row1}\n{row2}\n{row3}")


# ( or by another method (real method i messed up in first one))

row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]

map = [row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("where do you want to put your treasure?  ")

horizontal = int(position[0])
vertical =int(position[1])

selected_row = map[horizontal-1]    #this both lines can be redused to map[vertical-1][horizontal-1]="x" and code will work exactly the same
selected_row[vertical-1] = "x"

print(f"{row1}\n{row2}\n{row3}")