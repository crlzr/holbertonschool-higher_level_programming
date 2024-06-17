-- create a 2nd table second_table in the db hbtn_0c_0
-- id INT, name VACHAR(256), score INT
-- if it already exists, the script should not fail
-- not allowed to use SELECT AND SHOW

CREATE TABLE IF NOT EXISTS hbtn_0c_0.second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Insert data into the table

INSERT INTO hbtn_0c_0.second_table (id, name, score)
VALUES
(1, "John", 10),
(2, "Alex", 3),
(3, "Bob", 4),
(4, "George", 8);