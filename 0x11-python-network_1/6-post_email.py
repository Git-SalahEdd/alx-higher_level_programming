#!/usr/bin/python3
""" Python script that sends a POST request and displays the body. """
import requests
import sys

if __name__ == "__main__":
    text = requests.post(sys.argv[1], data={"email": sys.argv[2]}).text
    print(text)
