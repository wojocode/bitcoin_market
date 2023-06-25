import requests
import sys
import os

# get API_KEY from env variable - for safety reason 
# you can add this variable in your .bash_profile 
API_KEY = os.environ.get('API_KEY_EXCHANGE')

def check_currency():
    while True:
        try:
            currency = input("currency: ").upper().strip()
            response = requests.get(f"https://api.currencyapi.com/v3/latest?apikey={API_KEY}&currencies={currency}")
            if response.status_code == 200 and currency:
                response = response.json()
                return response['data'][currency]["value"], currency
            else:
                continue   
        except requests.RequestException:
            sys.exit("server doesn't response")  
    
def get_amount():
    while True:
        try:
            amount = float(input("bitcoin amount: ").strip())
            return amount
        except ValueError:
            print("invalid amount")

value = check_currency()
amount = get_amount()

# fetch data from coindeck 
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    bitcoin_response = response.json()
    bitcoin = bitcoin_response["bpi"]["USD"]["rate_float"]
    total = (bitcoin * amount) * value[0]
    print(f"{total:,.2f} {value[1]}")
except requests.RequestException:
    sys.exit()

