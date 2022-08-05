#!/usr/bin/python3
"""Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    query = """SELECT * FROM states
    WHERE name = %s
    ORDER BY states.id ASC"""
    c.execute(query, (argv[4],))
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()