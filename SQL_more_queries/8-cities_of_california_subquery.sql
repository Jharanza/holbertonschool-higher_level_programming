-- List all the cities of California --

SELECT cities.id, cities.name FROM cities JOIN states ON states.id = cities.state_id WHERE states.name = 'California'  ORDER BY cities.id ASC;
