-- create user user_0d_1 / all privileges / pw: user_0d_1_pwd
-- if user already exists, script should not fail

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';