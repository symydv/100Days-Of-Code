import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

news_apiKey = os.environ.get("NewApiKey")
stock_apiKey = os.environ.get("StockApiKey")





now  = datetime.now()
presentday = now.date()
if now.weekday() == 0:
    yesterday = presentday - timedelta(3)
    day_before_yesterday = yesterday - timedelta(1)
elif now.weekday() == 1:
    yesterday = presentday - timedelta(1)
    day_before_yesterday = presentday - timedelta(4)
elif now.weekday() == 7:
    yesterday = presentday - timedelta(2)
    day_before_yesterday = yesterday - timedelta(1)
else:
    yesterday = presentday - timedelta(1)
    day_before_yesterday = yesterday - timedelta(1)


##################################################################################################################################################
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=2O3UZXPAJOZPHMYF'
r = requests.get(url)
data = r.json()
yesterday_stock = data["Time Series (Daily)"][F"{yesterday}"]
day_before_yesterday_stock = data["Time Series (Daily)"][F"{day_before_yesterday}"]

print(yesterday_stock["1. open"])
percentage_drop = (float(day_before_yesterday_stock['4. close']) -float( yesterday_stock["1. open"]))*100/float(day_before_yesterday_stock['4. close'])

if percentage_drop >= 5:
    print(f"Price droped by {percentage_drop}%")
    print("GET NEWS")
print(day_before_yesterday_stock['4. close'])

################################################################################################################


news_url = (f'https://newsapi.org/v2/everything?q={COMPANY_NAME}&from=2025-03-12&sortBy=popularity&apiKey=6cd85f316003479b90235556140347e6')

req = requests.get(news_url)
resp = req.json()
print(resp)
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

##############################################################################################################################
from twilio.rest  import Client

Account_SID = "ACc88bcf1f901edb2e17095bb04dae5813"
Auth_token = "a25bee98f0d9ac46c3c451d30fae5f38"
Twilio_phone_number = "+16507191050"

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


#Half done no internet do it after some time..