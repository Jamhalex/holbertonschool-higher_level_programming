-- Lists all cities with their state names using a single SELECT
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id =  state.id
ORDER BY cities_id ASC;
