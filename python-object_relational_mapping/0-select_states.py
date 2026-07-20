#!/usr/bin/python3
"""
List all states from a MySQL database in ascending order by ID.
"""

import sys

import MySQLdb


def list_states(username, password, database):
    """
    Connect to MySQL and print every state ordered by its ID.
    """
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM states ORDER BY id ASC"
    )

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    connection.close()


if __name__ == "__main__":
    list_states(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    )
