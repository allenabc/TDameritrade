import requests
from config import td_consumer_key
import pprint

url=r"https://api.tdameritrade.com/v1/marketdata/chains"

symbol = 'AMD'
strike = 100
fromDate = '2021-10-15'
toDate = '2021-10-15'

params = {
    'apikey' : td_consumer_key,
    'symbol' : symbol,
    'strike' : strike,
    'fromDate' : fromDate,
    'toDate' : toDate,
}
#url = f"https://api.tdameritrade.com/v1/marketdata/AMD/quotes"
results = requests.get(url, params=params).json()
x = results['callExpDateMap']
pprint.pprint(x)
