import requests
from config import td_consumer_key
import pprint

url=r"https://api.tdameritrade.com/v1/marketdata/quotes"

symbol = 'AMD'

params = {
    'apikey' : td_consumer_key,
    'symbol' : symbol,
}
results = requests.get(url, params=params).json()
pprint.pprint(results)
#print(results[symbol]['description'])
#print(results[symbol]['lastPriceInDouble'])
