""" Write a Python program that implements a Shopping Cart system using OOP.
The program should:
  - Define a Product class with name and price
  - Define a ShoppingCart class that:
      - stores products
      - adds and removes products
      - calculates total price
      - displays all products
      - applies a discount to the total
  - Use a menu-based interface to interact with the user
  - Handle invalid input using try/except.   """

class Product:
    def __init__(self, name, price):
        if price <= 0:
            raise ValueError("Invalid price")
        self.name = name
        self.price = price

    def __str__(self):
        # Defines how the object is displayed when printed
        return f"{self.name} - {self.price} lei"


# Shopping cart class
class ShoppingCart:
    def __init__(self):
        self.__products = []

    # Add product to cart
    def add_product(self, product):
        if self.find_product(product.name):
            print("Product already exists in the cart!")
        else:
            self.__products.append(product)
            print("Product added successfully!")

    # Remove product from cart
    def remove_product(self, product):
        if not self.find_product(product.name):
            print("Product not found in cart!")
        else:
            self.__products.remove(product)
            print("Product removed successfully!")

    # Calculate total price
    def total(self):
        prices = []
        for product in self.__products:
            prices.append(product.price)
        return sum(prices)

    # Display products
    def show_products(self):
        if not self.__products:
            print("Cart is empty.")
            return

        for product in self.__products:
            print(product)

    # Apply discount
    def apply_discount(self, percent, total_amount):
        if percent <= 0 or percent > 100:
            raise ValueError("Invalid discount percentage")

        discount = percent / 100 * total_amount
        return total_amount - discount

    # Find product by name
    def find_product(self, name):
        for product in self.__products:
            if product.name == name:
                return product
        return None


def main():
    cart = ShoppingCart()

    while True:
        try:
            print("\nSHOPPING CART MENU:")
            print("\n1. Add product")
            print("2. Remove product")
            print("3. Apply discount")
            print("4. Show cart")
            print("5. Exit")

            option = int(input("\nChoose an option: "))

            if option == 1:
                name = input("Product name: ")
                price = float(input("Product price: "))
                product = Product(name, price)
                cart.add_product(product)

            if option == 2:
                name = input("Product name to remove: ")
                product = cart.find_product(name)
                cart.remove_product(product)

            if option == 3:
                total_value = cart.total()
                print("Total is:", total_value)

                percent = int(input("Enter discount percentage: "))
                result = cart.apply_discount(percent, total_value)

                print(
                    f"Original: {total_value}, Discount: {percent}%, Final price: {result}"
                )

            if option == 4:
                cart.show_products()

            if option == 5:
                print("Exit")
                break

        except ValueError:
            print("Invalid input!")

        except Exception as e:
            print("Unexpected error:", e)


if __name__ == "__main__":
    main()
