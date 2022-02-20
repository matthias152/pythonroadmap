#  scraps for data and writes it to csv file
from time import sleep
from csv import DictWriter
from bs4 import BeautifulSoup
import requests


BASE_URL = "https://quotes.toscrape.com"


def scrape_quotes():
    all_quotes = []
    url = "/page/1"
    while url:
        req = requests.get(f"{BASE_URL}{url}")
        soup = BeautifulSoup(req.text, "html.parser")
        SCRAPED_QUOTES = soup.find_all(class_="quote")
        for quote in SCRAPED_QUOTES:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"]
            })
        next_button = soup.find(class_="next")
        url = next_button.find("a")["href"] if next_button else None
        sleep(1)

    return all_quotes


# writing quotes to csv file
def write_quotes(z):
    with open("quotes.csv", "w", encoding="utf-8") as file:
        headers = ["text", "author", "bio-link"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for i in z:
            csv_writer.writerow(i)


quotes = scrape_quotes()
write_quotes(quotes)
