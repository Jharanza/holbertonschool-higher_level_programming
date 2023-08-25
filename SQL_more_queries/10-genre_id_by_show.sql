-- List all shows in the table
-- Show title and genre_id
SELECT ts.title, tsg.genre_id FROM tv_shows AS ts INNER JOIN tv_show_genres AS tsg WHERE ts.id = tsg.show_id ORDER BY ts.title, tsg.genre_id;
