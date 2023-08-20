-- Return the number of records
-- Keys GROUP BY, HAVING and ORDER BY
SELECT score, COUNT(score) AS `number` FROM second_table GROUP BY 1 HAVING COUNT(score) ORDER BY score DESC;
