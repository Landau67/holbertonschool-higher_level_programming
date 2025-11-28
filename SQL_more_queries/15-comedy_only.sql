-- Only Comedy
SELECT tv_shows.title
FROM tv_shows t
JOIN tv_show.genres ON t.id = tv_shows.genres.show.id
JOIN tv_genres ON tv_genres.id = tv_show.genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
