-- Lists all tv shows with their genre ID, including sahows withot genres
SELECT tv_shows.title, tv_show_genres_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genres_id ASC;
