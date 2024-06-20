#!/usr/bin/python3
"""
Script that takes the name of a state and lists all cities
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    for av in sys.argv:
        if av.count(";") > 0:
            exit()

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3]
                         )

    query = """SELECT cities.id, cities.name, states.name
            FROM cities
            INNER JOIN states
            ON cities.state_id = states.id
            WHERE BINARY state name = '{}'
            ORDER BY id ASC""".format(sys.argv[4])

    cur = db.cursor()
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)
