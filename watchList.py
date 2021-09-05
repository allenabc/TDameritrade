import requests
from config import td_consumer_key
import pprint

url=r"https://api.tdameritrade.com/v1/accounts/65462671/watchlists/"


params = {
    'apikey' : td_consumer_key,
}
results = requests.get(url, params=params)
pprint.pprint(results)
