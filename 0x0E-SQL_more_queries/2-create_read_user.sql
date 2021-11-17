-- Read user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' TO 'user_0d_2_pwd';
GRANT SELECT ONLY ON hbtn_0d_2.*;
