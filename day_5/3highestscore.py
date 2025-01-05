# we have to creat a code to get highest score in class without using max min function with help of loops

student_score = input("write the score of students \n").split()

for n in range(0,len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)    


highest_score = 0
for score in student_score:
    if score > highest_score:
        highest_score = score
print(f"the highest score is: {highest_score}")       