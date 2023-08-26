-- List all genres of the show Dexter
-- Each recod should display tv_genres.name
SELECT a.name FROM tv_genres AS a
LEFT JOIN tv_show_genres AS b
ON a.id = b.genre_id
LEFT JOIN tv_shows AS c
ON c.id = b.show_id
WHERE c.title  = 'Dexter'
ORDER BY a.name;
