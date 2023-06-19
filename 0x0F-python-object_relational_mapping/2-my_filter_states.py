#!/usr/bin/python3
"""This script lists all states that match the provided name"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    creates a cinnecteion to the database
    and queries for states that match the provided name
    """

    db = MySQLdb.connect(host='localhost', user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
        WHERE BINARY `name` = '{}' \
            ORDER BY states.id ASC".format(argv[4]))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
