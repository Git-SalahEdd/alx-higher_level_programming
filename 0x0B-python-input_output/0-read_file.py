#!/usr/bin/python3
"""Module to reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as file:
        read_file_data = file.read()
        print(read_file_data, end='')
