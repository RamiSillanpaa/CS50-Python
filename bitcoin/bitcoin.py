import requests
import sys
import json

try:
    count = sys.argv[1]
    try:
        if bool(float(count)):
            r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            j = json.loads(r.text)
            rate = j["bpi"]["USD"]["rate_float"]
            print(f"${float(count)*rate:,.4f}")
    except ValueError:
        sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command line argument")
except requests.RequestException:
    sys.exit("RequestException")