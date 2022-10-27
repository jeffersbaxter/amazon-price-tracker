from notify import send_email
from parse import get_price
from scrape import make_request
from utils import remove_non_ints

response = make_request()

price_str = get_price(response.text)
MAX_PRICE = 150.00
price = 0
try:
    price = float(price_str)
except ValueError:
    all_ints = remove_non_ints(price_str)
    price = float(all_ints)
finally:
    send_email(price)
