SELECT age, COUNT(id) as total_people
FROM people
GROUP BY age
HAVING COUNT(id) >= 10;

-- https://www.codewars.com/kata/58164ddf890632ce00000220/train/sql