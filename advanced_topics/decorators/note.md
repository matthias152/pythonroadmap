# Decorators
To funkcje, które jako argument przyjmują inną funkcje.
Pozwalają rozszerzyć istniejącą funkcje bez potrzeby modyfikacji oryginalnego kodu funkcji.

```
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")
```

Użycie *@my_decorator* to nic innego jak *say_whee = my_decorator(say_whee)*

Dobry przykład wykorzystania decorators do sprawdzania czasu funkcji:

```
from functools import wraps
from time import time

def speed_test(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		start_time = time()
		result = fn(*args, **kwargs)
		end_time = time()
		print(f"Executing {fn.__name__}")  # printing function name
		print(f"Time Elapsed: {end_time - start_time}")  # time passed
		return result
	return wrapper

@speed_test
def sum_nums_gen():
	return sum(x for x in range(90000000)) # generator

@speed_test
def sum_nums_list():
	return sum([x for x in range(90000000)]) # generator


print(sum_nums_gen())
print(sum_nums_list())
```
