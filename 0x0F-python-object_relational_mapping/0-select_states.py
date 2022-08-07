#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    c = db.cursor()

    c.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    rows = c.fetchall()

    for row in rows:
        print(row)
