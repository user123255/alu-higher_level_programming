-- Lists all shows and their genre IDs (if any) from the hbtn_0d_tvshows database
-- If a show does not have a genre, it will still appear with NULL

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
