# Web Scraping
udemy course section 31, 32, 33
Poprzez webscraping możemy "wykradać" dane ze stron do własnego użytku.

## BeautifulSoup
https://www.crummy.com/software/BeautifulSoup/bs4/doc/  
BeautifulSoup to moduł pomagający nam w webscrapingu.  

import:
```
import requests
from bs4 import BeautifulSoup
```
```
soup = BeautifulSoup(req.text, "html.parser")
```
Podstawowe funkcje:
Wysłanie zapytania do danej strony:
```
r = requests.get('https://api.github.com/events')
```
Możemy poruszać się po stronach sprawdzając ich kod źródłowy html
Aby znaleźć wszystkie elementy z klasą quote:
```
quotes = soup.find_all(class_="quote")
```
Jeśli chcemy uzyskać tekst widoczny na stronie używamy *get_text()*
```
for i in quotes:
    i.find(class_="text").get_text()
```

## CSV  
Z webscrapingiem przydatne mogą być np. pliki csv. Możemy do nich wpisywać bądź
czytać z nich dane.

import:
```
from csv import DictReader, DictWriter
```
Przykładowy wygląd pliku csv, dane oddzielone są zawsze przecinkami:

```
Name,Country,Height (in cm)
Ryu,Japan,175
Ken,USA,175
Chun-Li,China,165
```
Aby odczytać z pliku:
```
with open(filename, "r") as file:
    csv_reader = DictReader(file)
```
Aby wpisać dane do pliku:
```
with open("cats.csv", "w") as file:
	headers = ["Name", "Breed", "Age"]
	csv_writer = DictWriter(file, fieldnames=headers)
	csv_writer.writeheader()
	csv_writer.writerow({
		"Name": "Garfield",
		"Breed": "Orange Tabby",
		"Age": 10
	})
```
