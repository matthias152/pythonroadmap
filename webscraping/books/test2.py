#  https://quotes.toscrape.com/
import requests
from bs4 import BeautifulSoup
from random import choice


BASE_URL = "https://quotes.toscrape.com"


req = requests.get(f"{BASE_URL}")
soup = BeautifulSoup(req.text, "html.parser")
quotes = soup.find_all(class_="quote")
next_button = soup.find(class_="next")
url = next_button.find("a")["href"] if next_button else None

print(url)
