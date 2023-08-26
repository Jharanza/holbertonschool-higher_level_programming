-- List all genres and the numbers of shows linked to each
-- First column must be called genre and the second must be called number of shows
SELECT a.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres a  
LEFT JOIN tv_show_genres b
ON a.id = b.genre_id WHERE b.genre_id IS NOT NULL
GROUP BY a.name ORDER BY number_of_shows DESC;
