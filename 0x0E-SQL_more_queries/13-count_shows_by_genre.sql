-- Write a script that lists all genres from hbtn_0d_tvshows
SELECT name AS genre, COUNT(*) AS number_of_shows FROM tv_genres, tv_show_genres
WHERE id = genre_id
GROUP BY name
ORDER BY number_of_shows DESC;
