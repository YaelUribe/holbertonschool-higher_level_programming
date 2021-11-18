-- Number of shows by genre
SELECT tv_shows.name AS genre
COUNT(tv_show_genres.genre_id) AS number_of_shows FROM tv_genres
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
GROUP BY tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;

