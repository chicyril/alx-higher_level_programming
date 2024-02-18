#!/usr/bin/python3
"""List all states with a name starting with N (upper N) from the database
hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == '__main__':
    dbconn = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
    )
    dbcursor = dbconn.cursor()
    dbcursor.execute("""
                     SELECT * FROM states
                     WHERE name LIKE BINARY 'N%'
                     ORDER BY id ASC
                     """)
    dbres = dbcursor.fetchall()
    for row in dbres:
        print(row)
    dbcursor.close()
    dbconn.close()
