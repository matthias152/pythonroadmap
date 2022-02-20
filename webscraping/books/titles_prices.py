#  http://books.toscrape.com/
from bs4 import BeautifulSoup
import requests

BASE_URL = "http://books.toscrape.com"


def scraping():
    ALL_BOOKS = []
    url = "page-1.html"
    for i in range(1):
        req = requests.get(f"{BASE_URL}/catalogue/{url}")

        soup = BeautifulSoup(req.text, "html.parser")
        books = soup.find_all(class_="product_pod")
        for book in books:
            ALL_BOOKS.append({
                "title": book.h3.a["title"],
                "price": book.find(class_="price_color").get_text(),
            })
        # next_button = soup.find(class_="next")
        # url = next_button.find("a")["href"] if next_button else None
    return ALL_BOOKS


def counting():
    ALL_BOOKS_AVERAGE = []
    url = "page-1.html"
    for i in range(1):
        req = requests.get(f"{BASE_URL}/catalogue/{url}")

        soup = BeautifulSoup(req.text, "html.parser")
        books = soup.find_all(class_="product_pod")
        for book in books:
            PRICE = book.find(class_="price_color").get_text()
            PRICE = PRICE[2:]
            ALL_BOOKS_AVERAGE.append(
                float(PRICE)
            )
        # next_button = soup.find(class_="next")
        # url = next_button.find("a")["href"] if next_button else None
    average = sum(ALL_BOOKS_AVERAGE) / len(ALL_BOOKS_AVERAGE)
    print(f"Average price is: £{average}")
    return ALL_BOOKS_AVERAGE


# z = scraping()
# print(z)
counting()
