import requests
from config import td_consumer_key
import pprint

url=r"https://api.tdameritrade.com/v1/marketdata/chains"

symbol = 'AMD'

strike = 100

params = {
    'symbol':symbol,
    'strike':strike,
    'apikey':td_consumer_key,
    'fromDate':'2021-10-15',
    'toDate':'2021-10-15',
}
#url = f"https://api.tdameritrade.com/v1/marketdata/AMD/quotes"
results = requests.get(url, params=params).json()

x = results['callExpDateMap']

pprint.pprint(x)
