""" Exercise 1:
Write a Python program that:
  - asks the user for an email address
  - validates the email using a regular expression
  - accepts only emails ending in .com, .ro, or .net
  - prints whether the email is valid or invalid.   """

import re

email = input("What is your email? ").strip()

pattern = r"[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.(com|ro|net)"

if re.fullmatch(pattern, email, re.IGNORECASE):
    print("Valid email")
else:
    print("Invalid email")



""" Exercise 2:
Write a Python program that:
  - stores a multi-line text containing customer information
  - extracts key data using regular expressions:
  - email address
  - phone number
  - number of products ordered
  - total price
  - prints each extracted value separately.  """

import re

text = """
Client: Ana Popescu
Email: ana.popescu@gmail.com
Phone: 0722123456
Order: 3 products
Total price: 150 lei
"""

email = re.search(r"[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.(?:com|ro)", text, re.IGNORECASE)
phone = re.search(r"07\d{8}", text)
products = re.search(r"\d+ products", text)
price = re.search(r"\d+ lei", text)

print("Email:", email.group())
print("Phone number:", phone.group())
print("Number of products:", products.group())
print("Total price:", price.group())

