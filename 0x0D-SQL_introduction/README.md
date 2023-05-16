# SQL - Introduction

## Concepts
- [Databases](https://intranet.alxswe.com/concepts/37)

### **Resources**
- [What is Database & SQL?](https://intranet.alxswe.com/rltoken/yyRKTEdRkYEVlRgZPbasjw)
- [A Basic MySQL Tutorial](https://intranet.alxswe.com/rltoken/sV2PtK5YfQsXWW1malRZ5Q)
- [Basic SQL statements: DDL and DML](https://intranet.alxswe.com/rltoken/IUKo4-UaRZSKPvXr5u9oBw)
- [Basic queries: SQL and RA](https://intranet.alxswe.com/rltoken/rXKvu2u7vg1Hj6bnX7UgMg)
- [SQL technique: functions](https://intranet.alxswe.com/rltoken/-Riv_dzSYsJyvy-LlaO6Mg)
- [SQL technique: subqueries](https://intranet.alxswe.com/rltoken/QpIXoR--8eBIaidgSWYsBQ)
- [What makes the big difference between a backtick and an apostrophe?](https://intranet.alxswe.com/rltoken/Gt0nFJPJRwW2Y0izzwbVrw)
- [MySQL Cheat Sheet](https://intranet.alxswe.com/rltoken/1oU1LwCksQLXjs6fZYezrw)
- [MySQL 8.0 SQL Statement Syntax](https://intranet.alxswe.com/rltoken/HmdmLiYBM0Q34iCYPWd9XQ)
- [installing MySQL in Ubuntu 20.04](https://intranet.alxswe.com/rltoken/IpYI9rgbwfjxOAQQgpHCmQ)

## Learning Objectives
**General**
~~~

    What’s a database
    What’s a relational database
    What does SQL stand for
    What’s MySQL
    How to create a database in MySQL
    What does DDL and DML stand for
    How to CREATE or ALTER a table
    How to SELECT data from a table
    How to INSERT, UPDATE or DELETE data
    What are subqueries
    How to use MySQL functions

**More Info**

Comments for your SQL file:

$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$

Install MySQL 8.0 on Ubuntu 20.04 LTS

$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$

Connect to your MySQL server:

$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
~~~
| Tasks | Description |
| ----- | ----------- |
| 0. List databases | Write a script that lists all databases of your MySQL server. |
| 1. Create a database | Write a script that creates the database hbtn_0c_0 in your MySQL server. - If the database hbtn_0c_0 already exists, your script should not fail - You are not allowed to use the SELECT or SHOW statements |
| 2. Delete a database | Write a script that deletes the database hbtn_0c_0 in your MySQL server. - If the database hbtn_0c_0 doesn’t exist, your script should not fail - You are not allowed to use the SELECT or SHOW statements |
| 3. List tables | Write a script that lists all the tables of a database in your MySQL server. |
| 4. First table | Write a script that creates a table called first_table in the current database in your MySQL server. - first_table description: > id INT > name VARCHAR(256) - The database name will be passed as an argument of the mysql command - If the table first_table already exists, your script should not fail - You are not allowed to use the SELECT or SHOW statements |
| 5. Full description | Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server. - The database name will be passed as an argument of the mysql command |
| The database name will be passed as an argument of the mysql command | Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server. |
| 7. First add | Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server. - New row: > id = 89 > name = Best School |
| 8. Count 89 | Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server. |
| 9. Full creation | Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows. |
| 10. List by best | Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server. |
| 11. Select the best | Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server. |
| 12. Cheating is bad | Write a script that updates the score of Bob to 10 in the table second_table. |
| 13. Score too low | Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server. |
| 14. Average | Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server. |
| 15. Number by score | Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server. |
| 16. Say my name | Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server. |
| 17. Go to UTF8 | Write a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server |
| 18. Temperatures #0 | Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending). -Import in hbtn_0c_0 database this table dump: download |
| 19. Temperatures #1 | Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending) |
| 20. Temperatures #2 | Write a script that displays the max temperature of each state (ordered by State name). |
