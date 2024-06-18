-- create table unique ID (id INT with value 1 must be unique, name VARCHAR 256)
-- if unique_id already exists, script should not fail

CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);