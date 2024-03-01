#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
from sys import argv


if __name__ == "__main__":
    letter = "" if len(argv) == 1 else argv[1]
    payload = {"q": letter}
    url = "http://0.0.0.0:5000/search_user"

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()

        data = response.json()
        user_id = data.get("id")
        user_name = data.get("name")

        if user_id is not None and user_name is not None:
            print(f"[{user_id}] {user_name}")
        else:
            print("No result")
    except requests.exceptions.RequestException:
        print("No result")
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')
