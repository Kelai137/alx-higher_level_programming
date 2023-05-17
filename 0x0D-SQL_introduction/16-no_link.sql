-- list records not without a name value
SELECT score, name FROM second_table
WHERE NAME IS NOT NULL ORDER BY 1 DESC;
