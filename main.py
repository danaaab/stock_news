import requests
from numpy.distutils.conv_template import header
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "GWT6DQT3WDFK09KW"
NEWS_API_KEY = "74d7a0f4e0204f4e8308ebef4ce62ea7"

TWILIO_SID= "Your SID"
TWILIO_AUTO_TOKEN = "eb4b18bdaf2e1aeb40e494e9b79f414a"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]["4. close"]
previous_data = data_list[1]["4. close"]
price_difference = abs(float(yesterday_data) - float(previous_data))
percentage_difference = 100 * (price_difference/float(previous_data))
if percentage_difference > 1:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get(NEWS_ENDPOINT, params= news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)

    formatted_articles = [f"Headline:{article['title']} \nBrief: {article['description']}" for article in three_articles]
    client = Client(TWILIO_SID, TWILIO_AUTO_TOKEN)
    for article in  formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+16812305183",
            to="+48518532282",
        )




