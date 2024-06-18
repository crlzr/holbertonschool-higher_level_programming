-- import hbtn_0d_tvshows
-- list all shows contained in hbtn_0d_tvshows that have at least 1 genre linked


SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres
ON tv_shows.title = tv_show_genres.genres_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
