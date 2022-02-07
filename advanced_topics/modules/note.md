# Modules
Modules używamy aby nasz główny kod nie był za długi.

## Built-in Modules
Python gwarantuje wiele wbudowanych modułów, ich spis:  
https://docs.python.org/3/py-modindex.html

Przykładowe użycie:
```
import random
from termcolor import colored
```

## Import from another file
Sami również możemy tworzyć modules z funkcjami, a następnie wykorzystywać w innych programach
aby importować z innego pliku należy:
```
import <file name>
from <file name> import *
from <file name> import <function name>
```

## Packages i pip
Możemy korzystać z pakietów które stworzyli inni, znajdziemy je tutaj:
https://pypi.org/

aby je pobrać, używamy *pip*  

Przykład:
```
pip install pokemon
```
