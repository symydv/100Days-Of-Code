import smtplib
import datetime as dt
import pandas
import random

my_email = "symydv2005@gmail.com"
password = "alkx hdnj cbkj hwuf"

birthday = pandas.read_csv("day_32/birthdays.csv")

dict = birthday.to_dict(orient="records")

now = dt.datetime.now()
today = now.day  #to find todays date of month like 15
current_month = now.month
for i in dict:
    if today==i["day"] and current_month == i["month"]:
        file_path = f"day_32/letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_path) as file:
            lines = file.read()
            mail = lines.replace("[NAME]", i["name"]) 
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()  #tls - Transport Layer Security.Encrypt the message
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, 
                                    to_addrs = i["email"], 
                                    msg = f"Subject:Happy Birthday!\n\n{mail}"
                                    )
  
'''TO Run your python code on cloud you can use pythonanywhere 
    as you can not run this code every day for a year to check everyones birthday.'''
    
