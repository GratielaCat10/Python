""" 
Write a Python program that:
  - uses the CocktailDB API
  - takes a cocktail name as input
  - searches for the cocktail and retrieves its ID
  - fetches full cocktail details using the ID
Displays:
  - name
  - category
  - whether it is alcoholic
  - instructions
  - ingredients with measurements
Handles missing data and errors using try/except.   """

import requests

BASE_URL = "https://www.thecocktaildb.com/api/json/v1/1"


def search_cocktail(name):
    url = f"{BASE_URL}/search.php?s={name}"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    if not data or not data.get("drinks"):
        raise ValueError("Cocktail not found")

    return data["drinks"][0]["idDrink"]


def get_cocktail_info(cocktail_id):
    url = f"{BASE_URL}/lookup.php?i={cocktail_id}"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    return data["drinks"][0]


def display_cocktail_info(drink):
    print("\nCocktail information:")
    print("-" * 40)

    print(f"Category: {drink['strCategory']}")
    print(f"Alcoholic: {drink['strAlcoholic']}")
    print(f"Instructions: {drink['strInstructions']}")

    print("\nIngredients:")

    for i in range(1, 16):
        ingredient = drink.get(f"strIngredient{i}")
        measure = drink.get(f"strMeasure{i}")

        if ingredient:
            if measure:
                print(f"- {ingredient}: {measure}")
            else:
                print(f"- {ingredient}")


if __name__ == "__main__":
    cocktail = input("Enter cocktail name: ")

    try:
        cocktail_id = search_cocktail(cocktail)
        data = get_cocktail_info(cocktail_id)

        print("\nCocktail name:", data["strDrink"])
        display_cocktail_info(data)

    except Exception as e:
        print("Error:", e)

  
