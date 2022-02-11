# Object-oriented programming
udemy course section 24, 25, 26  

Główną koncepcją OOP jest powiązanie danych i funkcji, które na nie działają, jako jednej jednostki, tak aby żadna inna część kodu nie miała dostępu do tych danych.  

## Basics
Aby stworzyć nowy obiekt w pythonie używamy *class*
```
class User:
    pass
```
Danemu obiektowi możemy nadać parametry, które definiujemy w __init__
```
    class User:
        def __init__(self, name):
            self.name = name
```

## Methods
```
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, a):
        self.balance = self.balance + a
        return self.balance

    def withdraw(self, b):
        self.balance = self.balance - b
        return self.balance

acct = BankAccount("Sam")
acct.owner         #Sam
acct.balance       #0.0
acct.deposit(50)   #50
acct.withdraw(14)  #36
acct.balance       #36
```

## Inheritance
Obiekty mogą dziedziczyć od siebie parametry i metody.
```
class User:
    def __init__(self, name, lname, age):
        self.name = name
        self.lname = lname
        self.age = age

class Moderator(User):
    def __init__(self, name, lname, age, community):
        super().__init__(name, lname, age)
        self.community = community
```

## Dunder/Magic methods
```
class Train():
    def __init__(self, num_cars):
        self.num_cars = num_cars

    def __repr__(self):
        return "{} car train".format(self.num_cars)

    def __len__(self):
        return self.num_cars

newTrain = Train(7)
print(newTrain) # 7 car train
print(len(newTrain)) # 7
```
