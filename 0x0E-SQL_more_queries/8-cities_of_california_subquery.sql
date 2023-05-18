-- Lists all the cities of California found in a database
-- Lists all the cities of California found in hbtn_0d_usa

SELECT id, name
FROM cities
WHERE state_id = 1
ORDER BY id;
