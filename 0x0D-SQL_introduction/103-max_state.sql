-- max temp of each state ordered by state name
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY 1
ORDER BY 1;
