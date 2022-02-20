#  https://quotes.toscrape.com/
#  works the same but its reading data from csv file instead of scraping
import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader


BASE_URL = "https://quotes.toscrape.com"


def read_quotes(filename):
    with open(filename, "r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)


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
            print(f"Hint: The author was born on {birth_date} {birth_place}")
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


quotes = read_quotes("quotes.csv")
start_game(quotes)
