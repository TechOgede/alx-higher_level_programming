-- Lists all records in a table

-- Lists all records in second_table that have a 'name' value
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
