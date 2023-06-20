#!/usr/bin/python3
'''a script that lists all states from the database hbtn_0e_0_usa'''
import MySQLdb as _mysql
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Access: python3 0-select_states.py username \
              passwd database")
        sys.exit(1)

    password = sys.argv[1]
    username = sys.argv[2]
    database = sys.argv[3]

    db = _mysql.connect(host="localhost", passwd=password,
                        user=username, db=database, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
