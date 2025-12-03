import requests, os
from dotenv import load_dotenv
from twilio.rest import Client
import datetime as dt

load_dotenv()
STOCK_COMPANY = "TSLA"
COMPANY_NAME = "Tesla Inc"


# ---------------------------- Set Dates ------------------------------- #
def get_dates():
    yesterday = str(dt.date.today() - dt.timedelta(days=2))
    day_before_yesterday = str(dt.date.today() - dt.timedelta(days=3))

    return (yesterday, day_before_yesterday)


# ---------------------------- Sending SMS/Whatsapp Message ------------------------------- #
def send_sms_or_whatsapp(sms_or_whatsapp, message):
    twello_account_sid = os.getenv('TWELLO_ACCOUNT_SID')
    twello_auth_token = os.getenv('TWELLO_AUTH_TOKEN')
    client = Client(twello_account_sid, twello_auth_token)

    if sms_or_whatsapp == 0:
        from_number = 'whatsapp:+14155238886'
        to_number = 'whatsapp:+923463056137'
    else:
        from_number = '+15164478061'
        to_number = '+923463056137'

    message = client.messages.create(
        body=message,
        from_=from_number,
        to=to_number
    )
    print(message.status)


# ---------------------------- Get News------------------------------- #
def get_news(up_or_down, percentage):
    news_endpoint = 'https://newsapi.org/v2/everything'
    news_api_key = os.getenv('NEWS_API_KEY')
    news_params = {
        'q': COMPANY_NAME,
        'from': get_dates()[0],
        'sortBy': 'publishedAt',
        'apiKey': news_api_key
    }

    response2 = requests.get(url=news_endpoint, params=news_params)
    response2.raise_for_status()
    temp = response2.json()['articles'][:3]

    news = {}
    for i in temp:
        news[temp.index(i)] = {
            'title': COMPANY_NAME + f':  {up_or_down} {round(percentage, 2)}%',
            'headline': i['title'],
            'brief': i['description']
        }
    return news


# ---------------------------- Get Stock Data ------------------------------- #
def get_stock_data():
    stock_endpoint = 'https://www.alphavantage.co/query'
    stock_api_key = os.getenv('STOCK_API_KEY')
    stock_params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOCK_COMPANY,
        'apikey': stock_api_key
    }
    response = requests.get(url=stock_endpoint, params=stock_params)
    response.raise_for_status()

    yesterday = get_dates()[0]
    day_before_yesterday = get_dates()[1]

    stock_data = {k: v for k, v in response.json()['Time Series (Daily)'].items() if
                  k in (yesterday, day_before_yesterday)}

    closing_value_yes = float(stock_data[yesterday]['4. close'])
    closing_value_dby = float(stock_data[day_before_yesterday]['4. close'])

    # closing_value_yes = 334.0900
    # closing_value_dby = 329.3600

    return ((closing_value_yes - closing_value_dby) / closing_value_yes) * 100


# ---------------------------- Process ------------------------------- #
def process():
    up_or_down = 'Stable'
    diff_percentage = get_stock_data()

    if diff_percentage > 0.5 or diff_percentage < -5:

        up_or_down = "📈" if diff_percentage > 0.5 else "📉"

        tesla_news = get_news(up_or_down, diff_percentage)

        for i in tesla_news.values():
            message_body = f'{i["title"]}\n\nHeadline: {i["headline"]}\n\nBrief: {i["brief"]}'
            send_sms_or_whatsapp(0, message_body)


process()