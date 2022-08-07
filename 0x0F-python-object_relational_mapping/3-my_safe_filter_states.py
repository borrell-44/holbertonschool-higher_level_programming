#!/usr/bin/python3
"""Once again, write a script that takes in arguments
and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument. But
this time, write one that is safe from MySQL injections!"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    c = db.cursor()

    query = """SELECT * FROM states
    WHERE name = %s
    ORDER BY states.id ASC"""
    c.execute(query, (argv[4],))

    rows = c.fetchall()
    for row in rows:
        print(row)
