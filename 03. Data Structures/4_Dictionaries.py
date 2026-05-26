""" Exercise 1: Create a dictionary for a car with: brand , model.
Then: add a new key called year and remove the model key.
Print the final dictionary. """

car = {
    "brand": "Toyota",
    "model": "Corolla"
}

car["year"] = 2020

del car["model"]

print(car)



""" Exercise 2: Create a dictionary with employee names and salaries. Print each employee and salary using a loop. """

employees = {
    "John": 3000,
    "Emma": 3500,
    "Mike": 2800
}

for name, salary in employees.items():
    print(f"{name}: {salary}")



""" Exercise 3: Create a nested dictionary for 2 students.
Each student should have: name, age, grade
Print the grade of the first student. """

students = {
    "student1": {
        "name": "Alice",
        "age": 21,
        "grade": 9
    },
    "student2": {
        "name": "Bob",
        "age": 22,
        "grade": 8
    }
}

print(students["student1"]["grade"])



""" Exercise 4: Find the Most Frequent Word.
Given a sentence:
  - count all words
  - find the most frequent word.  """

sentence = "python is great and python is easy"

words = sentence.split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

most_frequent = max(word_count, key=word_count.get)

print("Word counts:", word_count)
print("Most frequent:", most_frequent)



""" Exercise 5: Create a nested dictionary for employees.
Each employee should contain:
  - department
  - salary
  - years_of_experience
Requirements:
  - print employees from IT department
  - find highest salary
  - calculate average salary.  """

employees = {
    "Alice": {
        "department": "IT",
        "salary": 5000,
        "experience": 3
    },
    "Bob": {
        "department": "HR",
        "salary": 4000,
        "experience": 5
    },
    "Emma": {
        "department": "IT",
        "salary": 6000,
        "experience": 4
    }
}

total_salary = 0

for name, data in employees.items():
    total_salary += data["salary"]

    if data["department"] == "IT":
        print("IT Employee:", name)

highest_paid = max(employees, key=lambda x: employees[x]["salary"])

average_salary = total_salary / len(employees)

print("Highest paid:", highest_paid)
print("Average salary:", average_salary)



""" Exercise 6: 
Create a dictionary where:
  - keys are student names
  - values are grades
Sort the dictionary by grades in ascending order and print the result. """


students = {
    "Alice": 88,
    "Bob": 72,
    "Emma": 95,
    "John": 81
}

sorted_students = dict(
    sorted(students.items(), key=lambda item: item[1])
)

print(sorted_students)

