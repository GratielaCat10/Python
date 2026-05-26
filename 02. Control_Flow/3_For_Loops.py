""" Exercise 1: Write a program that reads a name and:
  - Capitalizes the first letter of the name
  - Checks if the name contains the letter “a”
  - Prints the length of the name  """

name = input("Name: ")
name = name.capitalize()
print(name)

count = 0
for x in name:
    if x == "a" or x == "A":
        count = count + 1

if count >= 1:
    print("The name contains the letter a/A")
else:
    print("The name does not contain the letter a/A")

print("The length of the name is:", len(name))



""" Exercise 2: Given the list of numbers [4, 7, 10, 3, 8, 6], calculate the average without using sum(), then print all numbers greater than the average. """

numbers = [4, 7, 10, 3, 8, 6]

total = 0
for x in numbers:
    total = total + x

average = total / len(numbers)
print("The average is:", average)

print("Numbers greater than the average:")

for x in numbers:
    if x > average:
        print(x)



""" Exercise 3: Create a mini student catalog using two lists: one for student names and one for grades.
The program should:
  - allow adding students until the user types "stop"
Then display:
  - the student with the highest grade
  - the student with the lowest grade
  - the average grade of the class   """ 

students = []
grades = []

n = int(input("How many students do you want to enter? "))

for i in range(n):
    name = input("Enter student name: ")
    grade = int(input("Enter student grade: "))

    while grade < 1 or grade > 10:
        print("Invalid grade!")
        grade = int(input("Re-enter student grade: "))

    students.append(name)
    grades.append(grade)

if len(grades) == 0:
    print("No data available.")
else:
    highest_grade = max(grades)
    lowest_grade = min(grades)

    position_high = grades.index(highest_grade)
    position_low = grades.index(lowest_grade)

    print("Student with the highest grade is:", students[position_high])
    print("Student with the lowest grade is:", students[position_low])

    average = sum(grades) / len(grades)
    print("Class average is:", average)




