#!/usr/bin/python3
""" Python script that sends POST request and displays body of the response """
import urllib.request
import sys

if __name__ == "__main__":
    mail = {"email": sys.argv[2]}
    encoded_mail = urllib.parse.urlencode(mail).encode("ascii")
    req = urllib.request.Request(sys.argv[1], encoded_mail)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
