#!/usr/bin/python3
"""Write a script that lists all cities from the
database hbtn_0e_4_usa"""

if __name__ == "__main__":
    from sys import argv
    import sys
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    c = db.cursor()

    query = """SELECT cities.name
    FROM cities, states
    WHERE %s = states.name AND states.id = state_id
    ORDER BY cities.id ASC"""
    c.execute(query, (argv[4],))

    rows = c.fetchall()
    for i in range(len(rows)):
        sys.stdout.write(rows[i][0])
        if i != len(rows) - 1:
            print(",", end=" ")
    print()

    c.close()
    db.close()
