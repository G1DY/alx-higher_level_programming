-- a script that lists all cities contained in the database hbtn_0d_usa
SELECT cities.id, cities.name and states.name
FROM hbtn_0d_usa.cities and hbtn_0d_usa.states
ORDER BY cities.name ASC;

