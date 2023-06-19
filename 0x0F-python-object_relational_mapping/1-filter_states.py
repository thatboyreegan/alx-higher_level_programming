#!/usr/bin/python3
"""This script lists all states with a name that s
tarts with N from the database"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    creates access to the
    database and list all states starting with letter N
    """

    db = MySQLdb.connect(host='localhost', user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
        WHERE name LIKE BINARY 'N%' \
            ORDER BY states.id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
