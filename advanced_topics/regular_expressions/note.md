# Regular expressions  
udemy course section 34  
https://docs.python.org/3/library/re.html  
https://www.w3schools.com/python/python_regex.asp  

cheat-sheet: http://www.rexegg.com/regex-quickstart.html  
https://pythex.org/  

RegEx to sekwencja znaków którą możemy wyszukać w danym tekście.
Najczęściej używane są do wyszukiwania ciągów znaków w algorytmach i podmieniania ich,
bądź do weryfikowania danych wpisanych przez użytkownika (np. e-mail, karta kredytowa)

## Przykłady
Możemy tworzyć jakiekolwiek RegEx jakie chcemy, kilka przykładów:
```
"phone" - wyszukuje wszystko co ma w sobie słowo phone
"^The"  - wyszukuje wszystko co zaczyna się od The
"king&" - wyszukuje wszystko co kończy się na king
"^abcd$" - wyszukuje tylko i wyłącznie abcd
```
Braces:
```
"ab{2}" - string zaczynający się od a i kończący na bb ('abb')
"ab{2,}" - string zaczynający się od a i kończący na minimum dwa b ('abb', 'abbbb')
"ab{3,5}" - string zaczynający się od a i kończący na od 3 do 5 b ('abbb', 'abbbb', 'abbbbb')
```
Operator or | :
```
"hey|hi" - wyszukuje wszystko co ma w sobie hey albo hi
"(b|cd)ef" - string który zaczynaj się na b lub cd, konczacy na ef ('bef', 'cdef')
```
Bracket:
```
"^[a-zA-Z]" - string który zaczyna się od dowolnej litery
",[a-zA-Z0- 9]$" - string który kończy się na przecinku i dowolnej literze bądź cyfrze
```

## RegEx w pythonie
Aby wykorzystać RegEx w pythonie importujemy moduł re.  
Najważniejsze funkcje to:
```
import re
re.findall() - wyszukuje wszystkie zgodności i zwraca je w liście
re.split() - dzieli string przy kazdym matchu i zwraca jako liste
re.search() - po prostu wyszukuje
re.sub() - zamienia dane matche
```

Kilka przykładów:
```
# Program to extract numbers from a string

import re

string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string)
print(result)

# Output: ['12', '89', '34']
```

```
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x) # ['The', 'rain', 'in', 'Spain']
```

```
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x) # The9rain9in9Spain
```
