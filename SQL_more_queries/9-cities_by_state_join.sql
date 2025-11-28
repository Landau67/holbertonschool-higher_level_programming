-- Cities by States
SELECT cities.id , cities.name, states.name
FROM cities
RIGHT JOIN states ON state_id = cities.state_id
ORDER BY cities.id ASC;
