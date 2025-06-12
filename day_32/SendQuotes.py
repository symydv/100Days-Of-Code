import datetime as dt
import smtplib
import random

my_email = "symydv2005@gmail.com"
password = "xyia xqpt fawr ppkd"

date = dt.datetime.now()
day_of_week = date.weekday()

if day_of_week == 3:
    with open("day_32/quotes.txt") as quote_file:
        all_quotes =  quote_file.readlines() #returns a list
        quote = random.choice(all_quotes)

    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs="shyamyadav957586@gmail.com", msg=f"subject:Monday Motivation \n\n {quote}")

