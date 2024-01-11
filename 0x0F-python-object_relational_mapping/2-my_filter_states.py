#!/usr/bin/python3
"""
A script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )
    cursor = db.cursor()
    cmd = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
ORDER BY id".format(argv[4])
    cursor.execute(cmd)
    res = cursor.fetchall()
    for row in res:
        print(row)
    cursor.close()
    db.close()
