-- list all records >= 10 of the second_table, show name and best score first

SELECT name, score FROM hbtn_0c_0.second_table WHERE score >= 10 ORDER BY score DESC;
