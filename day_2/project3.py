# tis will tell you how many days weeks or months you have left to live if you live till 90 years of age

age=input("what is your current age ?\n")
years=90-int(age)
months=years*12
weeks=years*52
days=years*365
print(f"you have {days} days, {weeks} weeks, {months} months left.")
