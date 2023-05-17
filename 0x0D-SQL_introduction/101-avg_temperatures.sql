-- Displays average temperature by city

-- Displays average temperature by city from the table dump
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
