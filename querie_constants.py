save_request = """
insert into requests(
filter_field, keyword
)
value (%s, %s )
;
"""

ten_movies_rating = """
select title, year, genres, cast, runtime, `imdb.rating`
from movies
group by title, genres,  year, cast, runtime, `imdb.rating`
order by `imdb.rating` desc
limit %s; 
"""


movies_by_title = """
SELECT title, year, genres, cast, runtime, `imdb.rating`
FROM movies
WHERE title LIKE %s
group by title, genres,  year, cast, runtime, `imdb.rating`
order by `imdb.rating` desc
LIMIT %s;
"""

movies_by_genre_and_year = """
select title, year, genres, cast, runtime, `imdb.rating`
from movies
where  genres LIKE %s AND year = %s
group by title, genres,  year, cast, runtime, `imdb.rating`
order by `imdb.rating` desc
LIMIT %s;
"""


movies_by_rating = """
select title, year, genres, cast, runtime, `imdb.rating`
from movies
where `imdb.rating` >= %s
group by title, genres,  year, cast, runtime, `imdb.rating`
order by `imdb.rating` desc
LIMIT %s
;
"""

movies_by_cast = """
select title, year, genres, cast, runtime, `imdb.rating`
from movies
where cast LIKE %s
group by title, genres,  year, cast, runtime, `imdb.rating`
order by `imdb.rating` desc
LIMIT %s
;
"""

movies_by_keyword = """
select title, year, genres, cast, runtime, `imdb.rating`
from movies
where title LIKE %s or plot LIKE %s
group by title, genres,  year, cast, runtime, `imdb.rating`
order by `imdb.rating` desc
LIMIT %s

"""
popular_requests = """
SELECT filter_field,keyword,  COUNT(*) AS search_count
FROM requests
GROUP BY filter_field, keyword
ORDER BY search_count DESC
LIMIT %s;
"""

years_max_min = """
select max(year), min(year)
from movies;
"""