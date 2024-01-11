#!/usr/bin/python3
"""
A script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
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
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY \
'N%' ORDER BY id")
    res = cursor.fetchall()
    for row in res:
        print(row)
    cursor.close()
    db.close()
