
student_score= {
    "harry": 81,
    "ron": 78,
    "hermion": 99,
    "draco": 74,
    "neville" : 62,
}

students_grade = {}



#by me (just opposite bana di bhai tune)
# for key in student_score:
    
#     if student_score[key]<=70:
#         students_grade["fail"]= key
#     elif student_score[key]<=80:
#         students_grade["acceptable"]= key
#     elif student_score[key]<=90:
#         students_grade["exeeds expectation"]= key
#     else:
#         students_grade["outstanding"]=key

# print(students_grade)



#by ma'am
for student in student_score:
    score=  student_score[student]
    if score > 90:
        students_grade[student] = "outstanding"
    elif score > 80:
        students_grade[student] ="exceed expectation"
    elif score > 70:
        students_grade[student] = "acceptable"
    else:
        students_grade[student] = "fail"


print(students_grade)