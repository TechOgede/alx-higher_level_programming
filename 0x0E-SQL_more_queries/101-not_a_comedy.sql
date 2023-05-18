-- Lists all shows without a particular genre from a database
-- Lists all shows without the genre, Comedy, in the database hbtn_0d_tvshows
WITH comedy_shows AS (
    SELECT tv_shows.id, tv_shows.title
    FROM tv_shows 
    JOIN tv_show_genres
        ON tv_shows.id = tv_show_genres.show_id
    JOIN tv_genres
        ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy'
    )

SELECT tv_shows.title
FROM tv_shows
LEFT JOIN comedy_shows
    ON tv_shows.id = comedy_shows.id
WHERE comedy_shows.id IS NULL
ORDER BY tv_shows.title;
