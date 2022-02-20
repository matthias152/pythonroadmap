from bs4 import BeautifulSoup
import requests

BASE_URL = "http://books.toscrape.com"


req = requests.get(f"{BASE_URL}")
soup = BeautifulSoup(req.text, "html.parser")
books = soup.find_all(class_="product_pod")
next_button = soup.find(class_="next")
url = next_button.find("a")["href"]

print(url)
