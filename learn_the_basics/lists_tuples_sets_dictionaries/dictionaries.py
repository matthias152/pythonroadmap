# https://www.w3schools.com/python/python_dictionaries.asp
# udemy section 14

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x)  # before the change

car["color"] = "white"

print(x)  # after the change

y = car.values()


print(y)  # prints all values of dictionary


inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}
# Make a copy of inventory and save it to a variable called stock_list
stock_list = inventory.copy()
# add the value 18 to stock_list under the key "cookie"
stock_list['cookie'] = 18
# remove 'cake' from stock_list
stock_list.pop('cake')
