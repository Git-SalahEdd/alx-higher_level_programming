#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = argv[3]
    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=db, port=3306
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")
    res = cursor.fetchall()
    for row in res:
        print(row)
    cursor.close()
    db.close()
