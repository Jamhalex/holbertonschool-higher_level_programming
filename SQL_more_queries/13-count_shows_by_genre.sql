-- Lists all genres and the number of shows linked to each
-- Only shows genres with at least one linked show
-- Sorted by number of shows descending

SELECT
    genres.name AS genre,
    COUNT(tv_show_genres.show_id) AS number_of_shows
FROM genres
INNER JOIN tv_show_genres
ON genres.id = tv_show_genres.genre_id
GROUP BY genres.id
ORDER BY number_of_shows DESC;
