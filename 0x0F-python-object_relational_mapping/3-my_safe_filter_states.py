#!/usr/bin/python3
"""
free from sql injection
"""

import MySQLdb
import sys

if __name__ == "__main__":
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()
    exe = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    args = sys.argv[4]
    cur.execute(exe, (args,))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == sys.argv[4]:
            print(row)
    cur.close()
    con.close()
