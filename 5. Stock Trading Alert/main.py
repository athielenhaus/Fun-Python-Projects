import requests
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then get news.
parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : "xxxxxxxxxxx"
}

# get stock price data using API
response = requests.get("https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
data = response.json()

# set the desired date values
yesterday = datetime.now() - timedelta(1)
day_before = datetime.now() - timedelta(2)

yesterday = datetime.strftime(yesterday, '%Y-%m-%d')
day_before = datetime.strftime(day_before, '%Y-%m-%d')

# get the opening stock prices for the desired date values from the data
price_yesterday = float(data["Time Series (Daily)"][yesterday]["1. open"])
price_day_before = float(data["Time Series (Daily)"][day_before]["1. open"])

# get the percentage change. If absolute change >5%, multiple actions follow...
percentage_change = round((1-(price_yesterday/price_day_before))*100)
if -5 > percentage_change or percentage_change > 5:
    if percentage_change > 0:
        change = f"{percentage_change}% 🔺"
    else:
        change = f"{percentage_change}% 🔻"

    ## STEP 2: Use https://newsapi.org to get the first 3 news pieces for the COMPANY_NAME
    news_parameters = {
        "apiKey" : "xxxxxxxxxxxxx",
        "q": "Tesla"}
    
    # connect to API and get data
    response_news = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
    response_news.raise_for_status()
    news_data = response_news.json()
    
    # get first 3 articles
    top_three = news_data["articles"][:3]
    for article in top_three:
        article_title = article["title"]
        description = article["description"]

        ## STEP 3: Use https://www.twilio.com
        # Send a seperate message with the percentage change and each article's title and description to your phone number.
        account_sid = "xxxxxxxxxxx"
        auth_token = "xxxxxxxxxxxxxx"
        sending_number = "+14144090xxx"
        my_number = "+491782028xxx"
        
        # connect to API
        client = Client(account_sid, auth_token)
        
        # declare message content, sender and recipient
        message = client.messages \
                        .create(
                             body=f"TESLA: {change}\nHeadline: {article_title}\nBrief: {description}",
                             from_=sending_number,
                             to=my_number
                         )


