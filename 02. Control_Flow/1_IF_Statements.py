""" Exercise 1: A retail store applies discounts based on customer conditions.
  Write a Python program that reads the customer’s age, total order value, and loyalty card status (1 = yes, 0 = no), then prints the applicable discount:
   - No discount if the customer is under 18 or the order value is below 100
   - 20% discount if the customer has a loyalty card and the order value is at least 300
   - 10% discount if the customer has a loyalty card and the order value is between 100–299, or if they have no card but the order value is at least 500 """

age = int(input("Enter age: "))
order_value = int(input("Enter order value: "))
loyalty_card = int(input("Do you have a loyalty card? Enter 1 for yes, 0 for no: "))

if age < 18 or order_value < 100:
    print("No discount")
elif loyalty_card == 1 and order_value >= 300:
    print("20% discount")
elif (loyalty_card == 1 and 100 <= order_value <= 299) or (loyalty_card == 0 and order_value >= 500):
    print("10% discount")
else:
    print("Invalid data")



""" Exercise 2: An automated system validates and classifies messages sent to an educational platform.
  Write a Python program that reads the user’s age, a message, and whether the user is a teacher (1 = yes, 0 = no), then processes and analyzes the message:
    - Convert the message to lowercase
    - Replace all occurrences of “examen” with “test”
    - Create a reversed version of the message
Then compute:
  - message length
  - number of occurrences of “test”
  - first character, last character, and first character of the reversed message
Finally, print one result:
  - “Message blocked” if the user is under 16, or the message has fewer than 15 characters, or it starts with a digit
  - “Message approved” if the user is at least 16, is a teacher, “test” appears at most twice, and the message does not end with “!”
  - “Message for review” in all other cases """

age = int(input("Enter age: "))
message = input("Enter message: ")
teacher = int(input("Are you a teacher? (1 = yes, 0 = no): "))

message = message.lower()
message = message.replace("examen", "test")

reversed_message = message[::-1]

length = len(message)
occurrences = message.count("test")
first_char = message[0]
last_char = message[-1]
first_char_reversed = reversed_message[0]

if age < 16 or length < 15 or first_char.isdigit():
    print("Message blocked")

elif age >= 16 and teacher == 1 and occurrences <= 2 and last_char != "!":
    print("Message approved")

else:
    print("Message for review")



""" Exercise 3: An amusement park system determines visitor access based on input data.
Write a Python program that reads the visitor’s age, an access code, and ticket type (1 = standard, 2 = VIP), then processes the code:
  - Convert the code to lowercase
  - Replace all “#” characters with “@”
  - Create a reversed version of the code
Then analyze:
  - code length
  - number of “@” occurrences
  - first and last character
  - first character of the reversed code
Finally, print one result:
  - “Access denied” if the visitor is under 12, or the code has fewer than 10 characters, or it starts with a digit
  - “VIP access” if the visitor is at least 18, has a VIP ticket, “@” appears at most twice, and the first character of the reversed code is not a digit
  - “Standard access” in all other cases  """

age = int(input("Enter age: "))
access_code = input("Enter access code: ")
ticket_type = int(input("Ticket type (1 = standard, 2 = VIP): "))

access_code = access_code.lower()
access_code = access_code.replace("#", "@")

reversed_code = access_code[::-1]

length = len(access_code)
occurrences = access_code.count("@")
first_char = access_code[0]
last_char = access_code[-1]
first_char_reversed = reversed_code[0]

if age < 12 or length < 10 or first_char.isdigit():
    print("Access denied")

elif age >= 18 and ticket_type == 2 and occurrences <= 2 and not first_char_reversed.isdigit():
    print("VIP access")

else:
    print("Standard access")



