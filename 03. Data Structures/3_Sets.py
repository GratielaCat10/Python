""" Exercise 1: Check if list has duplicates. """

numbers = [1, 2, 3, 4, 4]

if len(numbers) == len(set(numbers)):
    print("All unique")
else:
    print("Duplicates found")



""" Exercise 2: Check if a username exists in a system (fast lookup). """

users = {"ana", "ion", "maria", "alex"}

name = input("Enter username: ")

if name in users:
    print("User exists")
else:
    print("User not found")



""" Exercise 3: Count unique website visitors. """

visits = ["u1", "u2", "u1", "u3", "u2", "u4"]

unique_visitors = set(visits)

print("Unique visitors:", len(unique_visitors))


