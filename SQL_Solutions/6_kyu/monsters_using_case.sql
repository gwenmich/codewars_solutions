SELECT t.id, t.heads, b.legs, t.arms, b.tails,
  CASE
    WHEN heads > arms OR tails > legs
    THEN 'BEAST'
    ELSE 'WEIRDO'
END AS species
FROM top_half as t
JOIN bottom_half as b
ON t.id = b.id
ORDER BY species;


-- https://www.codewars.com/kata/593ef0e98b90525e090000b9/train/sql