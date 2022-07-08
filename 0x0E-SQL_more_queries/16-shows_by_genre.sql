-- Write a script that lists all shows, and all genres linked to that show, from the database
SELECT title, name FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = genre_id
RIGHT JOIN tv_shows ON tv_shows.id = show_id
ORDER BY title, name ASC;
