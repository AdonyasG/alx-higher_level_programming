-- displays top 3 cities temp
SELECT city, AVG(value) AS avg_tmp FROM temperatures WHERE month=7 OR month=8 GROUP BY city ORDER BY avg_tmp DESC LIMIT 3;
~
