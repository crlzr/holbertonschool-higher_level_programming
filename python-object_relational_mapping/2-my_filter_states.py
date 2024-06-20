#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3]
                         )

    cur = db.cursor()

    query = """SELECT * FROM states
            WHERE name = '{}'
            ORDER BY id ASC""".format(sys.argv[4])


    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)
