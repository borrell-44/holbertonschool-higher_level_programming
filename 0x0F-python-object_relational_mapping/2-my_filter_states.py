#!/usr/bin/python3
""" Write a script that takes in an argument
and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument."""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    c = db.cursor()

    query = """SELECT * FROM states
    WHERE name = '{}'
    ORDER BY states.id ASC""".format(argv[4])
    c.execute(query)

    rows = c.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
