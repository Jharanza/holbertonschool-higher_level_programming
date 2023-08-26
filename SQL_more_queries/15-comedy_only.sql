-- List all Comedy shows
-- The id can be different
SELECT a.title FROM tv_shows a
LEFT JOIN tv_show_genres b ON a.id = b.show_id
LEFT JOIN tv_genres c ON c.id = b.genre_id
WHERE c.name = 'Comedy' ORDER BY a.title;
