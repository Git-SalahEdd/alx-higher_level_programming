#!/usr/bin/python3
""" Python script that displays the value of X-Request-Id """
import requests
import sys

if __name__ == "__main__":
    header = requests.get(sys.argv[1]).headers
    print(header.get("X-Request-Id"))
