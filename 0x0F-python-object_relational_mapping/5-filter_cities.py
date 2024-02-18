#!/usr/bin/python3
"""Takes in the name of a state as an argument and lists all cities of that
state, using the database hbtn_0e_4_usa."""
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
                   SELECT cities.name FROM cities
                   LEFT JOIN states ON cities.state_id = states.id
                   WHERE states.name = %s
                   ORDER BY cities.id ASC
                   """, (sys.argv[4],))

    dbres = dbcurs.fetchall()
    res = [row[0] for row in dbres]
    print(*res, sep=", ")
    dbcurs.close()
    dbconn.close()
