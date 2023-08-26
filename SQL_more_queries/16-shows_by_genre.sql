-- List all shows and genres linked to that show
-- If a show doesn't have a genre, display NULL
SELECT a.title, b.name
FROM tv_shows a 
LEFT JOIN tv_show_genres c 
ON a.id = c.show_id
LEFT JOIN tv_genres b
ON b.id = c.genre_id
ORDER BY a.title, b.name;
