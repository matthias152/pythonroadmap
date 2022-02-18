#  https://quotes.toscrape.com/
import requests
from bs4 import BeautifulSoup
from random import choice


BASE_URL = "https://quotes.toscrape.com"


def scrape_quotes():
    all_quotes = []
    url = "/page/1"
    while url:
        req = requests.get(f"{BASE_URL}{url}")
        soup = BeautifulSoup(req.text, "html.parser")
        quotes = soup.find_all(class_="quote")
        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"]
            })
        next_button = soup.find(class_="next")
        url = next_button.find("a")["href"] if next_button else None

    return all_quotes


def start_game(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    print("Here's a quote: ")
    print(quote['text'])
    print(quote['author'])
    guess = ''
    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(f"Who said this quote? Guesses remaining:{remaining_guesses} ")
        if guess.lower() == quote["author"].lower():
            print("You are right, good job!")
            break
        remaining_guesses -= 1
        if remaining_guesses == 3:
            res = requests.get(f"{BASE_URL}{quote['bio-link']}")
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Hint: The author was born on{birth_date} {birth_place}")
        elif remaining_guesses == 2:
            print(f"Hint: The author's first name starts with: {quote['author'][0]}")
        elif remaining_guesses == 1:
            last_initial = quote['author'].split(" ")[1][0]
            print(f"Hint: The author's last name starts with: {last_initial}")
    again = ''
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input("Play again? (y/n)")
    if again.lower() in ('yes', 'y'):
        return start_game(quotes)
    else:
        print("Bye!")


quotes = scrape_quotes()
start_game(quotes)
