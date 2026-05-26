""" Exercise 1: Find Maximum and Minimum. Find max and min without built-in functions. """

numbers = [7, 2, 10, 3, 8]

maximum = numbers[0]
minimum = numbers[0]

for n in numbers:
    if n > maximum:
        maximum = n
    if n < minimum:
        minimum = n

print(maximum)
print(minimum)



""" Exercise 2: Remove Duplicates. """

numbers = [1, 2, 2, 3, 4, 4, 5]

unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)

print(unique)



""" Exercise 3: Nested List (Student Grades). """

students = [
    ["Ana", 9],
    ["Ion", 7],
    ["Maria", 10]
]

for student in students:
    print(student[0], student[1])



""" Exercise 4: List Comprehension + Filtering. """

numbers = [2, 6, 8, 3, 10, 1]

filtered = [n for n in numbers if n > 5]

print(filtered)



""" Exercise 5: List Slicing Operations. """

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[0:3])
print(numbers[2:])
print(numbers[::-1])
