""" Exercise 1:
Write a Python program that:
  - reads data from a CSV file called students.csv
  - extracts student names and their hometowns
  - stores the data in a list of dictionaries
  - sorts the students alphabetically by name
  - prints each student in the format: "Name is from Home".  """

import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students.append({
            "name": row["name"],
            "home": row["home"]
        })

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")



""" Exercise 2:
Write a Python program that:
  - reads data from a file called students.csv
  - each row contains a student's name, home, and age
  - converts age to an integer
  - filters students whose age is greater than 18
  - prints only the names of those students.   """


import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students.append({
            "name": row["name"],
            "home": row["home"],
            "age": int(row["age"])
        })

print("Students older than 18:")

for student in students:
    if student["age"] > 18:
        print(student["name"])


