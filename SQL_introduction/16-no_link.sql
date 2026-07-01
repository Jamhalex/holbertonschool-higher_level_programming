-- Lists all records with a non-null name in descending order
SELECT score, name
FROM  second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

