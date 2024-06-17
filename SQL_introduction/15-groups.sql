-- list the number of records with the same score in second_table
-- result should display score, number of records for this score (number)
-- sorted (descending)

SELECT score, COUNT(*) AS number
FROM hbtn_0c_0.second_table
GROUP BY score
ORDER BY score DESC;
