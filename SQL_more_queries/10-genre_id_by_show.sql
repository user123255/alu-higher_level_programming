-- 10-genre_id_by_show.sql
-- Lists all shows with at least one genre linked
-- Format: tv_shows.title - tv_show_genres.genre_id
-- Sorted by tv_shows.title and then tv_show_genres.genre_id

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
