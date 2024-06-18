-- creates table force_name (id INT, name VARChAR(256), can't be NULL)
-- script shouldn't fail if force_name already exists

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);