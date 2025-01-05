height=float(input("what is your height in metre?"))
weight=float(input("what is your weight in kg?"))
BMI = round(weight/height**2,2)
print("your bmi is :" +str(BMI))
if BMI <=18.5:
    print("you are underweight")
elif BMI <= 25:
    print("you have a normal weight")
elif BMI <=30:
    print("you are obses")
elif BMI <=35:
    print("you are obese")
else:
    print("you are clinically obese")
