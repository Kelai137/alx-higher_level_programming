-- displays the avg temp(F) by city in descending order of temp
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY 1
ORDER BY 2 DESC;
