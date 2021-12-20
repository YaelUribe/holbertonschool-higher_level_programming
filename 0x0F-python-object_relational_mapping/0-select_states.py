#!/usr/bin/python3
"""Script for listing all states
from given database"""

if __name__ == "__main__":

    import sys
    import MySQLdb

    argv = sys.argv
    u_name = argv[1]
    passwd = argv[2]
    db_name = argv[3]

    data_base = MySQLdb.connect( # connect to MySQL
        host='localhost',
        port=3306,
        user=u_name,
        data_base=db_name)

    cursor = data_base.cursor() # create a cursor
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    values = cursor.fetchall()
    for i in values:
        print(i)
