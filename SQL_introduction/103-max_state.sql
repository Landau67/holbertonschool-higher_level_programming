-- Temperatures #2
SELECT state, MAX(value) as max_temp from temperatures GROUP BY state ORDER BY state;
