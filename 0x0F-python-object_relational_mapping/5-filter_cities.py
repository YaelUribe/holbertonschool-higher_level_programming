#!/usr/bin/python3
"""script that takes in the name of a state as an argument
and lists all cities of that state, using the given database"""

if __name__ == "__main__":

    import sys
    import MySQLdb

    argv = sys.argv
    u_name = argv[1]
    passwd = argv[2]
    db_name = argv[3]
    state = argv[4]

    db = MySQLdb.connect(  # connect to MySQL
        host='localhost',
        user=u_name,
        passwd=passwd,
        port=3306,
        db=db_name)

    cursor = db.cursor()  # create a cursor
    cursor.execute("""SELECT cities.name
                    FROM cities JOIN states
                    ON cities.state_id = states.id
                    WHERE states.name LIKE BINARY %(state)s
                    ORDER BY cities.id ASC""", {'state': state})
    values = cursor.fetchall()
    print(", ".join(map(lambda i: i[0], values)))
