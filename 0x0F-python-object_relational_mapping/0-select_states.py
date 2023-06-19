#!/usr/bin/python3
import MySQLdb as _mysql
import sys
"""a script that lists all states from the database hbtn_0e_0_usa"""


if __name__ == "__main__":
    db = _mysql.connect(host = "localhost", user = "sys.argv[1]",
                        passwd = "sys.argv[2]", db = "sys.argv[3]", port = 3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
