SELECT DISTINCT(people.name) FROM directors
JOIN people ON people.id = directors.person_id
JOIN movies ON movies.id = directors.movie_id
JOIN ratings ON ratings.movie_id = directors.movie_id

WHERE rating >= 9.0