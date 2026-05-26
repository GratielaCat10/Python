""" Exercise 1: Write a program that simulates a temperature sensor. The user manually inputs temperature values (integers). 
The program must evaluate each value and print:
  - “Heat the room” if temperature is below 18°C
  - “Cool the room” if temperature is above 26°C
  - “Optimal temperature” if temperature is between 18°C and 26°C
Requirements:
  - The user can input a maximum of 5 values
  - If the user enters 0, the program stops immediately  """

attempts = 0
temperature = -1

while temperature != 0 and attempts < 5:
    temperature = int(input("Enter room temperature (0 to stop): "))
    attempts += 1

    if temperature == 0:
        print("Monitoring stopped by user")
        break
    elif temperature < 18:
        print("Heat the room")
    elif temperature > 26:
        print("Cool the room")
    else:
        print("Optimal temperature")

if temperature != 0 and attempts == 5:
    print("5 attempts reached. Monitoring ended.")



""" Exercise 2: Write a program that simulates cinema ticket booking.
Requirements:
  - The cinema has 100 available seats
  - The user can attempt to buy tickets a maximum of 4 times
  - At each attempt, the user enters the number of tickets
Rules:
  - If the user enters 0 → print “Purchase cancelled” and stop
  - If requested tickets exceed available seats → print “Not enough seats”
  - If valid → subtract from total and print remaining seats
  - If seats reach 0 → print “No seats available” and stop   """

seats = 100
attempts = 0
tickets = -1

while tickets != 0 and seats != 0 and attempts < 4:
    tickets = int(input("How many tickets do you want? (0 to cancel): "))
    attempts += 1

    if tickets == 0:
        print("Purchase cancelled")
        break

    elif tickets > seats:
        print("Not enough seats")
    else:
        seats = seats - tickets
        print("Remaining seats:", seats)

if seats == 0:
    print("No seats available")
elif attempts >= 4:
    print("Maximum number of attempts reached")



""" Exercise 3: Write a program that simulates access to a computer lab.
Requirements:
  - The user selects a role: student (1) or professor (2)
  - If the user is a student, the program also asks for the year of study
  - The correct access code is: "informatica"
  - The user has a maximum of 3 attempts to enter the correct code
Rules:
  - If the user is a student and in year < 2 → print “Access denied” and stop
  - Professors have no year restriction
  - If the user enters "stop" → print “Access cancelled” and stop
  - If the code is incorrect → print “Wrong code”
  - If the code is correct → print “Access granted” and stop
  - After 3 failed attempts → print “Access blocked”  """

role = int(input("Are you a student or professor? (1 = student, 2 = professor): "))
correct_code = "informatica"
access_code = ""
attempts = 0

if role == 1:
    year = int(input("Enter year of study: "))

    if year < 2:
        print("Access denied")
    else:
        while access_code != "stop" and attempts < 3:
            access_code = input("Enter access code (type stop to cancel): ")
            attempts += 1

            if access_code == "stop":
                print("Access cancelled")
                break
            elif access_code != correct_code:
                print("Wrong code")
            else:
                print("Access granted")
                break

elif role == 2:
    while access_code != "stop" and attempts < 3:
        access_code = input("Enter access code (type stop to cancel): ")
        attempts += 1

        if access_code == "stop":
            print("Access cancelled")
            break
        elif access_code != correct_code:
            print("Wrong code")
        else:
            print("Access granted")
            break

if access_code != "stop" and access_code != correct_code and attempts >= 3:
    print("Access blocked")
  


""" Exercise 4: Write a program that simulates placing orders in a fast-food restaurant.
The menu is: menu = ["pizza", "burger", "salad", "pasta"]
Requirements:
  - The user can place a maximum of 5 orders
At each step:
  - enter a product name
  - if the user types "stop" → stop the program
Rules:
  - If the product is not on the menu → print "Product unavailable"
  - If the product exists → add it to the orders list
  - If the same product is ordered 3 times → print "Popular product!"
At the end, print:
  - the list of orders
  - the total number of ordered products using len()   """

menu = ["pizza", "burger", "salad", "pasta"]

orders = []
text = ""
attempts = 0

while text != "stop" and attempts < 5:
    text = input("What would you like to order? (type stop to quit): ")
    attempts += 1
    text = text.lower()

    if text == "stop":
        print("Order completed")
        break

    while text not in menu and text != "stop":
        print("Product unavailable!")
        text = input("What would you like to order?: ")

    if text in menu:
        orders.append(text)
        print("Product added to cart.")

remove_product = input("If you want to remove a product type YES, otherwise press enter: ")
remove_product = remove_product.lower()

if remove_product == "yes":
    while True:
        product = input("Which product do you want to remove? ")

        if product in orders:
            orders.remove(product)
            print(product, "was removed from the order.")
            break
        else:
            print("Product does not exist in the order! Try again.")

for n in menu:
    nr = orders.count(n)

    if nr >= 3:
        print(n, "is the most popular product")

print("Your order is:", orders)
print("You ordered", len(orders), "products.")

