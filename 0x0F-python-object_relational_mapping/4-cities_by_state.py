#!/usr/bin/python3
"""a script that takes in an argument and displays
   all values in the states table of hbtn_0e_0_usa
   where name matches the argument
"""
import MySQLdb as _mysql
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = _mysql.connect(host="localhost", user=username,
                        passwd=password, db=database, port=3306)
    cur = db.cursor()
    cur.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    [print(city) for city in cur.fetchall()]
