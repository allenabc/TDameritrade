import requests
from config import td_consumer_key
import pprint

url=r"https://api.tdameritrade.com/v1/instruments/"

url = "https://api.tdameritrade.com/v1/BOND/hours"
url = "https://api.tdameritrade.com/v1/marketdata/DJI/movers"

params = {
    'apikey' : td_consumer_key,
}
results = requests.get(url, params = params).json()

pprint.pprint(results)
