""" 
Create a calculator with:
  - addition
  - subtraction
  - multiplication
  - division.    """


num1 = float(input("First number: "))
num2 = float(input("Second number: "))

operation = input("Choose operation (+ - * /): ")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation")
