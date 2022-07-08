-- Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT name FROM tv_genres, tv_show_genres, tv_shows
WHERE title = "Dexter"
AND tv_genres.id = genre_id
AND tv_shows.id = show_id
GROUP BY name
ORDER BY name ASC;
