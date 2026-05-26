""" Exercise 1: Conditional Counting
Write a function called count_even_numbers that:
  - receives n
  - returns how many even numbers are between 1 and n.  """

def count_even_numbers(number):
    even_numbers = []

    for x in range(1, number):
        if x % 2 == 0:
            even_numbers.append(x)

    return len(even_numbers)

print(count_even_numbers(7))



""" Exercise 2: 
Write a function called count_vowels() that:
  - reads a word from the user
  - counts how many vowels the word contains
  - returns the total number of vowels.  """

def count_vowels():
    vowels = ["a", "e", "i", "o", "u"]
    
    word = input("Enter a word: ")
    
    total = 0

    for letter in word:
        if letter in vowels:
            total = total + 1

    return total

print("This word contains", count_vowels(), "vowels")



""" Exercise 3: 
Write a function called get_max() that:
  - receives a list of numbers
  - finds the largest number in the list
  - returns the maximum value.   """

numbers = [4, 8, 2, 15, 6]

def get_max(numbers_list):
    maximum = numbers_list[0]

    for number in numbers_list:
        if number > maximum:
            maximum = number

    return maximum

print(get_max(numbers))



""" Exercise 4: 
Write a function called fizzbuzz() that:
  - receives a number n
  - loops through numbers from 1 to n
Replaces:
  - multiples of 3 with "Fizz"
  - multiples of 5 with "Buzz"
  - multiples of both 3 and 5 with "FizzBuzz"
  - returns the final list.   """

def fizzbuzz(n):
    result = []

    for i in range(1, n + 1):

        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")

        elif i % 3 == 0:
            result.append("Fizz")

        elif i % 5 == 0:
            result.append("Buzz")

        else:
            result.append(i)

    return result

print(fizzbuzz(n))

