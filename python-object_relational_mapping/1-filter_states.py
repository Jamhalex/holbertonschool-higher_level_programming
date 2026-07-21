#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from the database.

The script connects to a MySQL database using MySQLdb and displays
all states whose names begin with the uppercase letter 'N',
sorted by id in ascending order.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states "
        "WHERE name LIKE 'N%' "
        "ORDER BY id ASC"
    )

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()
