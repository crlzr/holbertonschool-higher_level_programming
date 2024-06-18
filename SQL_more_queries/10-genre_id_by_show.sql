-- import hbtn_0d_tvshows
-- list all shows contained in hbtn_0d_tvshows that have at least 1 genre linked


SELECT title, genre_id
FROM hbtn_0d_tvshows
JOIN tv_genres
ON tv_shows.title = tv_show_genres.genre_id
ORDER BY title ASC;
