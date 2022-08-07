#!/usr/bin/python3
"""Write script that lists all states with a
name starting with N (upper N) from the database hbtn_0e_0_usa"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         password=argv[2], database=argv[3])
    c = db.cursor()

    c.execute("""SELECT * FROM states
    WHERE name LIKE 'N%'
    ORDER BY states.id ASC""")

    rows = c.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
