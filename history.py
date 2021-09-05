import requests
from config import td_consumer_key
import pprint
import datetime

url = "https://api.tdameritrade.com/v1/marketdata/AMD/pricehistory"
st= datetime.datetime(2021, 8,1).strftime('%s')
et= datetime.datetime(2021, 9,2).strftime('%s')

params = {
    'apikey' : td_consumer_key,
    'startDate' : st,
#    'endDate' : et,
    'period': 2
}
results = requests.get(url, params = params).json()

pprint.pprint(results)
