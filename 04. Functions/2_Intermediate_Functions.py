""" Exercise 1: 
Write a function called longest_substring() that:
  - receives a string
  - finds the length of the longest substring without repeating characters
  - returns the maximum length.  """

s = "lcstpmmlcst"


def longest_substring(string):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(string)):

        while string[right] in char_set:
            char_set.remove(string[left])
            left += 1

        char_set.add(string[right])
        max_length = max(max_length, right - left + 1)

    return max_length

print(longest_substring(s))



""" Exercise 2: 
Write a function called max_subarray_length() that:
  - receives a list of integers and a target sum k
  - finds the length of the longest subarray whose sum equals k
  - returns that maximum length.  """

nums = [1, -1, 5, -2, 3, 1, 2, -4, -2, 2]
k = 3

def max_subarray_length(nums, k):
    prefix_map = {}
    prefix_sum = 0
    max_length = 0

    for i, num in enumerate(nums):
        prefix_sum += num

        if prefix_sum == k:
            max_length = i + 1

        if (prefix_sum - k) in prefix_map:
            max_length = max(max_length, i - prefix_map[prefix_sum - k])

        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i

    return max_length

print(max_subarray_length(nums, k))



""" Exercise 3: 
Write a function called get_repetitions() that:
  - receives a string
  - counts how many times each character appears in the string
  - returns a dictionary with character frequencies.   """

s = "banana"


def get_repetitions(string):
    repetitions = {}

    for char in string:
        repetitions[char] = repetitions.get(char, 0) + 1

    return repetitions

print(get_repetitions(s))



""" Exercise 4: 
Write a function called find_missing_numbers() that:
  - receives a list of integers
  - finds the minimum and maximum values in the list
  - identifies all missing numbers in the range
  - returns a list of missing numbers.  """

nums = [18, 19, 20, 21, 23, 25]

def find_missing_numbers(numbers):
    start = min(numbers)
    end = max(numbers)
    missing = []

    for i in range(start, end + 1):
        if i not in numbers:
            missing.append(i)

    return missing

print(find_missing_numbers(nums))



""" Exercise 5: Write a function called first_unique_char() that:
  - receives a string
  - finds the first character that appears only once in the string
  - returns its index
  - returns -1 if no such character exists. """

  s = "leetcode"
def first_unique_char(string):
    frequency = {}

    # count character occurrences
    for char in string:
        frequency[char] = frequency.get(char, 0) + 1

    # find first character with frequency 1
    for index, char in enumerate(string):
        if frequency[char] == 1:
            return index

    return -1
  
print(first_unique_char(s))



""" Exercise 6: Write a function called two_sum() that:
  - receives a list of numbers and a target value
  - finds two numbers whose sum is equal to the target
  - returns the indices of those two numbers. """


nums = [2, 11, 7, 15]
target = 9


def two_sum(numbers, target):
    seen_numbers = {}

    for index, number in enumerate(numbers):
        complement = target - number

        if complement in seen_numbers:
            return [seen_numbers[complement], index]

        seen_numbers[number] = index


print(two_sum(nums, target))
