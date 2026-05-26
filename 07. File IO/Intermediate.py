""" 
Write a Python program that:
  - manages a car database stored in a CSV file
  - allows adding, deleting, editing, and searching cars
  - stores cars with fields: brand, model, year
  - supports sorting cars by year
  - displays all cars in a clean format
  - uses csv.DictReader and csv.DictWriter
  - handles file errors and invalid input gracefully.  """


import csv
import os


def add_car():
    brand = input("Brand: ")
    model = input("Model: ")
    year = input("Year: ")

    if os.path.exists("cars.csv"):
        with open("cars.csv") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["Brand"] == brand and row["Model"] == model and row["Year"] == year:
                    answer = input("This car already exists. Do you still want to add it? (y/n): ")
                    if answer.lower() == "n":
                        print("Adding cancelled!")
                        return
                    break

    with open("cars.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Brand", "Model", "Year"])

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow({
            "Brand": brand,
            "Model": model,
            "Year": year
        })

    print("Car successfully added!")


def delete_car():
    brand = input("Brand: ")
    model = input("Model: ")
    year = input("Year: ")

    try:
        with open("cars.csv", "r") as file:
            reader = csv.DictReader(file)
            cars = list(reader)

        updated_cars = []
        found = False

        for car in cars:
            if car["Brand"] == brand and car["Model"] == model and car["Year"] == year:
                found = True
            else:
                updated_cars.append(car)

        if not found:
            print("Car not found!")
            return

        with open("cars.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Brand", "Model", "Year"])
            writer.writeheader()
            writer.writerows(updated_cars)

        print("Car deleted!")

    except FileNotFoundError:
        print("No cars available!")


def edit_car():
    brand = input("Brand: ")
    model = input("Model: ")
    year = input("Year: ")
    new_year = input("New year: ")

    try:
        with open("cars.csv", "r") as file:
            reader = csv.DictReader(file)
            cars = list(reader)

        found = False

        for car in cars:
            if car["Brand"] == brand and car["Model"] == model and car["Year"] == year:
                car["Year"] = new_year
                found = True

        if not found:
            print("Car not found!")
            return

        with open("cars.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Brand", "Model", "Year"])
            writer.writeheader()
            writer.writerows(cars)

        print("Year updated!")

    except FileNotFoundError:
        print("No cars available!")


def sort_by_year():
    try:
        with open("cars.csv", "r") as file:
            reader = csv.DictReader(file)
            cars = list(reader)

        if not cars:
            print("No cars available!")
            return

        cars.sort(key=lambda car: int(car["Year"]))

        for car in cars:
            print(f"{car['Brand']} | {car['Model']} | {car['Year']}")

    except FileNotFoundError:
        print("No cars available!")


def show_cars():
    try:
        with open("cars.csv", "r") as file:
            reader = csv.DictReader(file)
            cars = list(reader)

        if not cars:
            print("No cars available!")
            return

        for car in cars:
            print(f"{car['Brand']} | {car['Model']} | {car['Year']}")

    except FileNotFoundError:
        print("No cars available!")


def search_car():
    brand = input("Brand: ")
    found = False

    try:
        with open("cars.csv", "r") as file:
            reader = csv.DictReader(file)

            for car in reader:
                if car["Brand"] == brand:
                    print(f"Car details: {car['Brand']} | {car['Model']} | {car['Year']}")
                    found = True
                    break

            if not found:
                print("Car not found!")

    except FileNotFoundError:
        print("No cars available!")


while True:
    try:
        print("\nCARS MENU")
        print("1. Add car")
        print("2. Delete car")
        print("3. Edit car")
        print("4. Sort cars by year")
        print("5. Show cars")
        print("6. Search car")
        print("7. Exit")

        option = int(input("\nChoose option: "))

        if option == 1:
            add_car()
        elif option == 2:
            delete_car()
        elif option == 3:
            edit_car()
        elif option == 4:
            sort_by_year()
        elif option == 5:
            show_cars()
        elif option == 6:
            search_car()
        elif option == 7:
            print("Goodbye!")
            break

    except ValueError:
        print("Invalid input!")

    except Exception as e:
        print(f"Error: {e}")


