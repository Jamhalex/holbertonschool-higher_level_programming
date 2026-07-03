-- Lists all genres of the show Dexter
-- Results sorted by genre name ascending

SELECT
    genres.name
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
INNER JOIN genres
ON genres.id = tv_show_genres.genre_id
WHERE tv_shows.title = "Dexter"
ORDER BY genres.name ASC;
