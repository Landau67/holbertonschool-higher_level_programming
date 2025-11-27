-- Temperatures #1
SELECT city, AVG(value) as avg_temp FROM temperatures WHERE month IN (7,8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
