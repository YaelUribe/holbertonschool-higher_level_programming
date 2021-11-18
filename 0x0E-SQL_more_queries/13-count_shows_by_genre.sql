-- Number of shows by genre
SELECT tv.name AS genre,
COUNT(tv_show_genres.genre_id) AS number_of_shows FROM tv_genres AS tv
JOIN tv_show_genres ON tv.id = tv_show_genres.show_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
