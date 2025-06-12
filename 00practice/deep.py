import random

def select_EC252HW2problems():

    problem_nos = list(range(1, 61))
   
    user_input = int(input("Enter the last two digits of your Roll Number"))
               
    # Give seed such that same result is obtained every time for given roll no
    random.seed(user_input)
   
    # Select 10 random problems
    selected_problems = sorted(random.sample(problem_nos, 15))

    return selected_problems

selected_problems = select_EC252HW2problems()    
print("Your 15 selected problems are:", selected_problems)
print("Please Submit the solution of these problems before the deadline")