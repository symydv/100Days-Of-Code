# SMTP - Simple Mail Transfere Protocol.

import smtplib

my_email = "symydv2005@gmail.com"
password = "New@password123" #this is app password we have generated for gmail in settings.
with smtplib.SMTP("smtp.gmail.com") as connection: #smtp.gmail.com is smtp adress of google's email

    '''after writing "with" keyword you dont have to close it at end. 
    If you dont use it you have to use connections.close()'''
    
    connection.starttls()  #tls - Transport Layer Security.Encrypt the message
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, 
                        to_addrs="shyamyadav957586@gmail.com", 
                        msg="subject:Hello\n\nThis is body of may email"
                        )


import datetime as dt

now = dt.datetime.now()  #this gets you current date and time
year = now.year
day_of_week = now.weekday()
print(day_of_week) # 0 means monday and so on

date_of_bearth = dt.datetime(year=2005,month=7,day=23)
print(date_of_bearth)

