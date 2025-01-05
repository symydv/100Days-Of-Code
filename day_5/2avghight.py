#without using len or sum function we have to calculate avg hight using loops



student_heights = input("input a list of student heights\n").split()

for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)



total_height = 0
for height in student_heights:
   total_height = total_height + height
   


number_of_students = 0
for student in student_heights:
    number_of_students += 1


avg = total_height/number_of_students
print(f"the avg hight is {avg}")