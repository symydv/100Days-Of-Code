import random
names = ["shyam", "anuj", "bhanu", "shivam" ,"nikhil"]

students_score = {student:random.randint(1,100) for student in names}
print(students_score)


passed_student = {student:score for (student, score) in students_score.items() if score>59 }
print(passed_student)
 
##################################################################
sentence = "what is the airspeed velocity of an unloden swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)

################################################################
weather_c ={
"monday":12,
"tuesday":14,
"wednesday":15,
"thursday":14,
"friday":21,
"saturday":22,
"sunday":24,
}

weather_f = {day:(temp*9/5)+32 for (day, temp) in weather_c.items()}
print(weather_f)


####################################################################3
import pandas
student_dict = {
    "student": ["angela", "james", "lily"],
    "score": [56, 76, 98]
}
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#loop through rows of dataframe

for (index, row) in student_data_frame.iterrows():
    print(row.student)  #also try row.score and only row.

