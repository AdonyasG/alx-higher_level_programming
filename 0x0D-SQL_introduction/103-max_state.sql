-- displays max tmp
SELECT state, AVG(value) AS max_temp FROM temperatures GROUP BY state ORDER BY max_temp;
