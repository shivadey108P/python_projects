import requests
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_api_key = os.environ.get('STOCK_API_KEY')

stock_end_point = 'https://www.alphavantage.co/query'
news_stock_api_key = os.environ.get('NEWS_API_KEY')
news_endpoint = 'https://newsapi.org/v2/everything'
TWILIO_SID = os.environ.get('TWILIO_ACC_SID')
TWILIO_API_KEY = os.environ.get('TWILIO_AUTH_TOKEN')

news_parameters = {
    'apiKey' : news_stock_api_key,
    'qInTitle' : COMPANY_NAME
}

stocks_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol' : STOCK,
    'outputsize': 'compact',
    ''
    'apikey' : stock_api_key
}

stocks_response = requests.get(url=stock_end_point, params=stocks_parameters)
stocks_response.raise_for_status
data = stocks_response.json()

stocks = data['Time Series (Daily)']
stocks_list = [value for (key, value) in stocks.items()]
yesterday_closing_price = float(stocks_list[0]['4. close'])
day_before_yesterday_closing_price = float(stocks_list[1]['4. close'])
# print(yesterday_closing_price)
# print(day_before_yesterday_closing_price)

increase = False
if yesterday_closing_price > day_before_yesterday_closing_price:
    increase = True
    
if increase:
    percent = f"🔼 {round((yesterday_closing_price-day_before_yesterday_closing_price)/ yesterday_closing_price * 100, 2)}%"
    percentage = round((yesterday_closing_price-day_before_yesterday_closing_price)/ yesterday_closing_price * 100, 2)
else:
    percent = f"🔻 {(round((day_before_yesterday_closing_price-yesterday_closing_price)/yesterday_closing_price *100, 2))* -1}%"
    percentage = (round((day_before_yesterday_closing_price-yesterday_closing_price)/yesterday_closing_price *100, 2))* -1
    

if abs(percentage) > 0.5:
    news_response = requests.get(url=news_endpoint, params=news_parameters)
    news_response.raise_for_status
    articles = news_response.json()['articles']
    three_articles = articles[:3]
    formatted_article_list = [f"Headline: {article['title']}\nBrief: {article['description']}" for article in three_articles]
    client = Client(TWILIO_SID, TWILIO_API_KEY)
    for article in formatted_article_list:
        message = client.messages.create(
            body= f"{STOCK}: {percent}\n{article}",
            from_='+12562033607',
            to='+918555914966'
        )
        # print(article)
    print(message.status)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


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

