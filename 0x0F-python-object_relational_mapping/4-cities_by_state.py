#!/usr/bin/python3
"""Write a script that lists all cities from the database
hbtn_0e_4_usa"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    c = db.cursor()

    query = """SELECT cities.id, cities.name, states.name
    FROM cities, states
    WHERE states.id = state_id
    ORDER BY cities.id ASC"""
    c.execute(query)

    rows = c.fetchall()
    for row in rows:
        print(row)

    c.close()
    db.close()
