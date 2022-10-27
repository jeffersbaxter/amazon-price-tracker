from bs4 import BeautifulSoup
import lxml


def get_price(text):
    soup = BeautifulSoup(text, "lxml")
    el = soup.find(name="span", class_="a-offscreen")
    return el.getText()
