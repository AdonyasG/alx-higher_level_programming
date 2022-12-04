#!/usr/bin/python3
"""
list cities under passed argument states
"""

import MySQLdb
import sys

if __name__ == "__main__":
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()
    exe = """SELECT cities.name FROM cities
            INNER JOIN states ON cities.state_id=states.id
            WHERE states.name = %s ORDER BY cities.id ASC"""
    args = sys.argv[4]
    cur.execute(exe, (args,))
    args = [','.join(row) for row in cur]
    print(', '.join(args))
    cur.close()
    con.close()
