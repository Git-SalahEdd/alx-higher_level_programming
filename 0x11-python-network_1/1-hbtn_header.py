#!/usr/bin/python3
""" Python script that displays the value of the X-Request-Id variable. """
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as req:
        info = req.info()
        print(info.get("X-Request-Id"))
