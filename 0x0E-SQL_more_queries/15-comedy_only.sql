-- Write a script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT title FROM tv_shows, tv_show_genres, tv_genres
WHERE name = "Comedy"
AND tv_genres.id = genre_id
AND show_id = tv_shows.id
ORDER BY title ASC;
