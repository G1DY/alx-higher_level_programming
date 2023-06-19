#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """lists all states with a name starting with N (upper N)"""
    db = MySQLdb.connect(host="localhost", user="sys.argv[1]", port=3306,
                         passwd="sys.argv[2]", db="sys.argv[3]")
    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                WHERE name LIKE BINARY '%n' \
                ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
