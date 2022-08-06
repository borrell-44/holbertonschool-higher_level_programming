#!/usr/bin/python3
"""Write a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa where
name matches the argument"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    c = db.cursor()
    query = f"""SELECT * FROM states
    WHERE name = '{argv[4]}'
    ORDER BY states.id ASC"""
    c.execute(query)
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
