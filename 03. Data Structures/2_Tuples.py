""" Exercise 1: Convert tuple to list, modify, then convert back. """

numbers = (1, 2, 3, 4)

temp = list(numbers)
temp.append(5)

numbers = tuple(temp)

print(numbers)



""" Exercise 2: Given student tuples, print only students with grade ≥ 8. """

students = (("Ana", 9), ("Ion", 7), ("Maria", 10))

for name, grade in students:
    if grade >= 8:
        print(name, grade)



""" Exercise 3: Find the most expensive product. """

products = (("milk", 5), ("bread", 3), ("coffee", 12), ("rice", 7))

max_product = products[0]

for item in products:
    if item[1] > max_product[1]:
        max_product = item

print(max_product)


