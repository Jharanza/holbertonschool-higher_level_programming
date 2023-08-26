-- List all shows
-- If show doesn't have a genre, display NULL
SELECT a.title, b.genre_id FROM tv_shows a LEFT JOIN tv_show_genres b ON a.id = b.show_id ORDER BY a.title, b.genre_id;
