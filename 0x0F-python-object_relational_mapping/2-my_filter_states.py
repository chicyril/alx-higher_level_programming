#!/usr/bin/python3
"""Takes in arguments and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == '__main__':
    dbconn = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )
    dbcursor = dbconn.cursor()
    dbcursor.execute("""
                     SELECT * FROM states
                     WHERE name LIKE BINARY '{}'
                     ORDER BY id ASC
                     """.format(sys.argv[4]))
    dbres = dbcursor.fetchall()
    for row in dbres:
        print(row)
    dbcursor.close()
    dbconn.close()
