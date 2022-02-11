# we want to take nubmers list and put their squared result to another list
# without map
numbers = [1, 2 ,3, 4, 5]
squared_nums = []

square = lambda n: n**2

for i in numbers:
    squared_nums.append(square(i))

print(squared_nums)

# using map

squared_nums2 = list(map(lambda n: n**2, numbers))

print(squared_nums2)

num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1+n2, num1, num2)

print(list(result))  # [9, 11, 13]


def myfunc(a, b):
    return a + b


x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

print(list(x))
