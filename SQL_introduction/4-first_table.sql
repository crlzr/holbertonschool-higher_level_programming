-- write a script that creates a table called first_table in the current database
-- first_table (id INT, name VARCHAR(256)) - shouldn't fail if first_table already exists
-- not allowed to use SELECT or SHOW

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);