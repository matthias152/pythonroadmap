# udemy section 12
# https://www.w3schools.com/python/python_lists.asp

list1 = ["apple", "banana", "cherry"]
print(list1[1]) # prints second element of the list

# prints last element of the list
list2 = ["apple", "banana", "cherry"]
print(list2[-1]) # banana


# prints third, fourth, fifth elements of the list
list3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list3[2:5]) # ['cherry', 'orange'. 'kiwi']


# hecks if something is in the list

list4 = ["apple", "banana", "cherry"]
if "apple" in list4:
  print("Yes, 'apple' is in the fruits list")


# Create a list called instructors
instructors = []

# Add the following strings to the instructors list
    # "Colt"
    # "Blue"
    # "Lisa"
instructors.extend(["Colt", "Blue", "Lisa"])

# Remove the last value in the list
instructors.pop()

# Remove the first value in the list
instructors.pop(0)

# Add the string "Done" to the beginning of the list
instructors.insert(0, 'Done')
