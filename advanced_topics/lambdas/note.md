# Lambdas
Source: https://www.w3schools.com/python/python_lambda.asp  
https://www.w3schools.com/python/ref_func_map.asp  
https://www.geeksforgeeks.org/python-map-function/
udemy course section 20

Lambda to mała funkcja, która przyjmuje dowolną liczbę argumentów.

Jeden argument:
```
x = lambda a : a + 10
print(x(5)) # 15
```
```
cube = lambda num: num ** 3
cube(3) # 27
cube(8) # 512
```

Dwa argumenty:
```
x = lambda a, b : a * b
print(x(5, 6)) # 30
```

Lambdy możemy używać w środku innych funkcji:
```
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
```

## Map

Syntax:
```
map(func, iter)
```
Map wykonuje funkcje dla każdego przedmiotu w danej liście
```
def myfunc(a, b):
    return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

print(list(x))  #['appleorange', 'bananalemon', 'cherrypineapple']
```

Dobrze działa z funkcją *lambda*

```
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result)) #  [2, 4, 6, 8]
```

## Filter

Dzięki *filter()* możemy filtrować dane listy stawiając warunki:

```
names = ["Austin", "Sam", "Anthony", "Angel", "Bill"]
a_names = list(filter(lambda n: n[0] == 'a', names))  # we check if first char is a
print(a_names)  # ["Austin", "Anthony", "Angel"]
```
