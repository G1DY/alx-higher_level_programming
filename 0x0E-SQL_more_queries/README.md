# SQL - More queries 

## **Resources**
- [How To Create a New User and Grant Permissions in MySQL](https://intranet.alxswe.com/rltoken/RniBKj48bnIN8xpXhGl1yA)
- [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://intranet.alxswe.com/rltoken/FIiEIvA6IN_hSKM5TvgyxQ)
- [MySQL constraints](https://intranet.alxswe.com/rltoken/LrovGa6N-OE2ID_tpWZRaQ)
- [SQL technique: subqueries](https://intranet.alxswe.com/rltoken/kR71h5zjkPtx4kBoVf7q0g)
- [Basic query operation: the join](https://intranet.alxswe.com/rltoken/rNMJeQ1jbNTCljbvCSjf6w)
- [SQL technique: multiple joins and the distinct keyword](https://intranet.alxswe.com/rltoken/HhZ6TJ1q5S0aR4lhfpKdOQ)
- [SQL technique: join types](https://intranet.alxswe.com/rltoken/T6FZUQdsMzr8hgNInBzudA)
- [SQL technique: union and minus](https://intranet.alxswe.com/rltoken/Nd-sdM8QUpf0YKIlXzVv4w)
- [MySQL Cheat Sheet](https://intranet.alxswe.com/rltoken/iSNyinU6SPWTGDUWMmcRkg)
- [The Seven Types of SQL Joins](https://intranet.alxswe.com/rltoken/-plhBsra0N7BOuFoEg--zg)
- [MySQL Tutorial](https://intranet.alxswe.com/rltoken/I4Lws_eQrIrNTbkZvvk-oQ)
- [SQL Style Guide](https://intranet.alxswe.com/rltoken/051eAEP_rePBU7jeh879GA)
- [MySQL 8.0 SQL Statement Syntax](https://intranet.alxswe.com/rltoken/YavbYiraYFr8oTukT_N6eQ)
- [Design](https://intranet.alxswe.com/rltoken/EWLRPeqr5sQ9AqfoG_KXxw)
- [Normalization](https://intranet.alxswe.com/rltoken/mqBhYoSYbhH5ZZrhDcY0kA)
- [ER Modeling](https://intranet.alxswe.com/rltoken/R0exkJmf-2ddKjGfa8D0dA)

## **Learning Objectives**
~~~
    How to create a new MySQL user
    How to manage privileges for a user to a database or table
    What’s a PRIMARY KEY
    What’s a FOREIGN KEY
    How to use NOT NULL and UNIQUE constraints
    How to retrieve datas from multiple tables in one request
    What are subqueries
    What are JOIN and UNION

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

Use “container-on-demand” to run MySQL

In the container, credentials are root/root

    Ask for container Ubuntu 20.04
    Connect via SSH
    OR connect via the Web terminal
    In the container, you should start MySQL before playing with it:

$ service mysql start
 * Starting MySQL database server mysqld
$
$ cat 0-list_databases.sql | mysql -uroot -p
Database
information_schema
mysql
performance_schema
sys
$

In the container, credentials are root/root
**How to import a SQL dump**

$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password:
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password:
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password:
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
~~~
| Tasks | Description |
| ----- | ----------- |
| 0. My privileges! | Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost). |
| 1. Root user | Write a script that creates the MySQL server user user_0d_1 - user_0d_1 should have all privileges on your MySQL server - The user_0d_1 password should be set to user_0d_1_pwd - If the user user_0d_1 already exists, your script should not fail |
| 2. Read user | Write a script that creates the database hbtn_0d_2 and the user user_0d_2. - user_0d_2 should have only SELECT privilege in the database hbtn_0d_2 - The user_0d_2 password should be set to user_0d_2_pwd - If the database hbtn_0d_2 already exists, your script should not fail - If the user user_0d_2 already exists, your script should not fail |
| 3. Always a name | Write a script that creates the table force_name on your MySQL server - force_name description: id INT name VARCHAR(256) can’t be null - The database name will be passed as an argument of the mysql command - If the table force_name already exists, your script should not fail |
| 4. ID can't be null | Write a script that creates the table id_not_null on your MySQL serve id INT with the default value 1 , name VARCHAR(256), The database name will be passed as an argument of the mysql command, If the table id_not_null already exists, your script should not fail |
| 5. Unique ID | Write a script that creates the table unique_id on your MySQL server., everything else as number 4 except: id INT with the default value 1 and must be unique |
| 6. States table | Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server., id INT unique, auto generated, can’t be null and is a primary key, name VARCHAR(256) can’t be null |
| 7. Cities table | Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server., id INT unique, auto generated, can’t be null and is a primary key, state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table, name VARCHAR(256) can’t be null |
| 8. Cities of California | Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa, The states table contains only one record where name = California (but the id can be different, as per the example), Results must be sorted in ascending order by cities.id, You are not allowed to use the JOIN keyword |
| 9. Cities by States | Write a script that lists all cities contained in the database hbtn_0d_usa, Each record should display: cities.id - cities.name - states.name, Results must be sorted in ascending order by cities.id, You can use only one SELECT statement |
| 10. Genre ID by show | Import the database dump from hbtn_0d_tvshows to your MySQL server:[download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql), Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked 1. Each record should display: tv_shows.title - tv_show_genres.genre_id 2. Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id 3. You can use only one SELECT statement |
| 11. Genre ID for all shows | Import the database dump of hbtn_0d_tvshows to your MySQL server:[download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)Write a script that lists all shows contained in the database hbtn_0d_tvshows 1. Each record should display: tv_shows.title - tv_show_genres.genre_id 2. Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id 3. If a show doesn’t have a genre, display NULL 4. You can use only one SELECT statement |
| 12. No genre | Import as no.11 and Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked, 1.Each record should display: tv_shows.title - tv_show_genres.genre_id 2. Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id 3. You can use only one SELECT statement |
| 13. Number of shows by genre | import as number 11 and Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each, 1. Each record should display: <TV Show genre> - <Number of shows linked to this genre>, 2. First column must be called genre 3. Second column must be called number_of_shows 4. Don’t display a genre that doesn’t have any shows linked 5. Results must be sorted in descending order by the number of shows linked 6. You can use only one SELECT statement |
| 14. My genres | import as no.11 and Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter, 1. The tv_shows table contains only one record where title = Dexter (but the id can be different), 2. Each record should display: tv_genres.name, 3. Results must be sorted in ascending order by the genre name 4. You can use only one SELECT statement |
| 15. Only Comedy | import as no.11 and Write a script that lists all Comedy shows in the database hbtn_0d_tvshows, 1. The tv_genres table contains only one record where name = Comedy (but the id can be different), 2. Each record should display: tv_shows.title, 3. Results must be sorted in ascending order by the show title, 4. You can use only one SELECT statement |
| 16. List shows and genres | import as 11 and Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows, 1. If a show doesn’t have a genre, display NULL in the genre column, 2. Each record should display: tv_shows.title - tv_genres.name 3. Results must be sorted in ascending order by the show title and genre name, 4. You can use only one SELECT statement |
| 17. Not my genre | import as 11 and Write a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter, 1. The tv_shows table contains only one record where title = Dexter (but the id can be different), 2. Each record should display: tv_genres.name, 3. Results must be sorted in ascending order by the genre name, 4. You can use a maximum of two SELECT statement |
| 18. No Comedy tonight! | import as previous and Write a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows, 1. The tv_genres table contains only one record where name = Comedy (but the id can be different), 2. Each record should display: tv_shows.title, 3. Results must be sorted in ascending order by the show title, 4. You can use a maximum of two SELECT statement |
| 19. Rotten tomatoes | Import the database hbtn_0d_tvshows_rate dump to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql), Write a script that lists all shows from hbtn_0d_tvshows_rate by their rating, 1. Each record should display: tv_shows.title - rating sum 2. Results must be sorted in descending order by the rating, 3. You can use only one SELECT statement |
| 20. Best genre | import as 19 and Write a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating, 1. Each record should display: tv_genres.name - rating sum, 2. Results must be sorted in descending order by their rating, 3. You can use only one SELECT statement |
