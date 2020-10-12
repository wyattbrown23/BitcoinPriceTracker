#API key and starter code found here: https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time

def get_bitcoin_price():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start':'1',
        'limit':'1',
        'convert':'USD'
    }

    headers = {
        'Accepts':'application/json',
        'X-CMC_PRO_API_KEY': ''
    }

    session=Session()
    session.headers.update(headers)

    try:
        starttime = time.time()
        last_price = -1
        while True:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            price = data['data'][0]['quote']["USD"]['price']
            price = str(round(price, 3))
            daily_percentage_change = data['data'][0]['quote']["USD"]['percent_change_24h']
            last_update = data['data'][0]['quote']["USD"]['last_updated']

            if price != last_price:
                print("bitcoin current price: ", "$", price)
                print("Percentage change last 24 hours: ", daily_percentage_change)
                print("Last updated: ", last_update, "\n")
                last_price = price
            time.sleep(60.0 - ((time.time() - starttime) % 60.0))
    except(ConnectionError, Timeout, TooManyRedirects, KeyError) as e:
        print(e)

def main():
    get_bitcoin_price()

main()