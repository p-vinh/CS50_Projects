SELECT movies.title FROM stars
JOIN movies ON movies.id = stars.movie_id
JOIN people ON people.id = stars.person_id

WHERE people.name = 'Johnny Depp' AND movies.title IN(
	SELECT movies.title FROM stars
	JOIN movies ON movies.id = stars.movie_id
	JOIN people ON people.id = stars.person_id
	WHERE people.name = "Helena Bonham Carter"
);