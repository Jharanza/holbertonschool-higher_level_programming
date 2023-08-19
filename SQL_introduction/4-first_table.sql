-- Create a table with conditionals to avoid errors and columns 
-- We add columns id and name
CREATE TABLE IF NOT EXISTS first_table
(
	id	INT,
	name 	VARCHAR(256)
);
