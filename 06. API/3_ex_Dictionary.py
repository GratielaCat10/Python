""" 
Write a Python program that:
  - uses the Free Dictionary API
  - takes a word as input from the user
Allows two options:
  - get the first definition of the word
  - get up to 5 meanings (part of speech, definition, example)
Uses functions to structure the logic.
Handles errors using try/except.
Displays results in a clean, readable format.   """

import requests

BASE_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"


def get_exact_word_data(word):
    url = f"{BASE_URL}{word}"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    if not data or not data[0]:
        raise ValueError("Word not found")

    return data[0]


def get_all_meanings(word):
    url = f"{BASE_URL}{word}"
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError("Word not found")

    data = response.json()

    if not isinstance(data, list) or len(data) == 0:
        raise ValueError("Word not found")

    entry = data[0]
    meanings = entry.get("meanings", [])

    results = []
    count = 0

    for meaning in meanings:
        part_of_speech = meaning.get("partOfSpeech", "unknown")

        for definition in meaning.get("definitions", []):
            results.append({
                "partOfSpeech": part_of_speech,
                "definition": definition.get("definition", "No definition"),
                "example": definition.get("example", "No example")
            })

            count += 1
            if count == 5:
                return results

    return results


def show_word_details(data):
    print("\nWord information:", data["word"])
    print("-" * 30)

    print("Definition:", data["meanings"][0]["definitions"][0]["definition"])

    first_def = data["meanings"][0]["definitions"][0]
    example = first_def.get("example", "No example")
    print("Example:", example)


def show_meanings_list(meanings):
    print("\nWord meanings:")
    print("-" * 30)

    for item in meanings:
        print(item)


def main():
    while True:
        print("\n1. Get word definition")
        print("2. Get all meanings")
        print("3. Exit")

        option = input("Choose option: ")

        if option == "1":
            word = input("Enter word: ")
            try:
                data = get_exact_word_data(word)
                show_word_details(data)
            except Exception as e:
                print("Error:", e)

        if option == "2":
            word = input("Enter word: ")
            try:
                meanings = get_all_meanings(word)
                show_meanings_list(meanings)
            except Exception as e:
                print("Error:", e)

        if option == "3":
            print("Exit")
            break


if __name__ == "__main__":
    main()
  
