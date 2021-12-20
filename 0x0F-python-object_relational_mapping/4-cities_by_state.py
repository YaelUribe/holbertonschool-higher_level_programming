#!/usr/bin/python3
"""Script for listing all cities by state
from given database"""

if __name__ == "__main__":

    import sys
    import MySQLdb

    argv = sys.argv
    u_name = argv[1]
    passwd = argv[2]
    db_name = argv[3]

    db = MySQLdb.connect(  # connect to MySQL
        host='localhost',
        user=u_name,
        passwd=passwd,
        port=3306,
        db=db_name)

    cursor = db.cursor()  # create a cursor
    cursor.execute("""SELECT cities.id, cities.name, states.name
                    FROM cities JOIN states
                    ON cities.state_id = states.id
                    ORDER BY cities.id""")
    values = cursor.fetchall()
    for i in values:
        print(i)
