#!/usr/bin/python3
"""
Display states whose name matches a user-provided value safely.

This script connects to a MySQL database and uses a parameterized
query to prevent SQL injection.
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
        "WHERE BINARY name = %s "
        "ORDER BY id ASC",
        (sys.argv[4],)
    )

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    db.close()
