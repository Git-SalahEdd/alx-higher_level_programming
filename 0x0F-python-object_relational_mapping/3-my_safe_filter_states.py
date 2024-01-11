#!/usr/bin/python3
"""
A script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
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
    cmd = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cursor.execute(cmd, (argv[4],))
    res = cursor.fetchall()
    for row in res:
        print(row)
    cursor.close()
    db.close()
