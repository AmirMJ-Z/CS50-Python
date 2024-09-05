import sys
import requests

if len(sys.argv) != 2:
    sys.exit('Missing command-line argument')

try:
    num = float(sys.argv[1])

except:
    sys.exit('Command-line argument is not a number')

price = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()['bpi']['USD']['rate_float']
price = num * price

print(f'${price:,.4f}')




