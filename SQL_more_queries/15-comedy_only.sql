-- Only Comedy
SELECT tv_shows.title
FROM tv_shows
JOIN tv_shows.genres ON tv_shows.id = tv_shows.genres.show.id
JOIN tv_genres ON tv_genres.id = tv_show.genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
