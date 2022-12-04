#!/usr/bin/python3
"""
filters ciry by state
"""

import MySQLdb
import sys

if __name__ == "__main__":
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()
    cur.execute("""SELECT cities.id, cities.name,states.name
                FROM cities INNER JOIN states
                ON cities.state_id=states.id ORDER BY cities.id ASC""")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    con.close()
