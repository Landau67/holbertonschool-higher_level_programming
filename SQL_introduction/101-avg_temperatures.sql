-- Temperatures #0
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY avg_temp ORDER BY avg_temp DESC;
