-- Create table with columns id and name
-- Column id must have a default value and be unique
CREATE TABLE IF NOT EXISTS unique_id
(
	id	INT DEFAULT 1 UNIQUE,
	name	VARCHAR(256)
);
