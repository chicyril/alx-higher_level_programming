#!/usr/bin/python3
"""List all states from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == '__main__':
    dbconn = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    dbcurs = dbconn.cursor()
    dbcurs.execute("""
                   SELECT cities.id, cities.name, states.name FROM cities
                   JOIN states ON cities.state_id = states.id
                   ORDER BY id ASC
                   """)

    dbres = dbcurs.fetchall()
    for row in dbres:
        print(row)

    dbcurs.close()
    dbconn.close()
