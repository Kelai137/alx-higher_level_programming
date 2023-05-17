-- list number of records with the same score in table
SELECT score,  COUNT(score) AS number FROM second_table GROUP BY 1 ORDER BY 2 DESC;
