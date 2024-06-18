-- list all the cities of California that can be found in db hbtn_0d_usa

USE hbtn_0d_usa
SELECT *
FROM cities
WHERE name = "California"
ORDER BY cities.id;