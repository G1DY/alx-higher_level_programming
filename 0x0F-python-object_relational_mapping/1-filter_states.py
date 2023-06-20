#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Access using: paython3 filename \
              passwd username database")
    password = sys.argv[1]
    username = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in cur.fetchall() if state[1][0] == "N"]
