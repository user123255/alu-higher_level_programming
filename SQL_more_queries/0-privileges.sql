-- Ensure user_0d_1 exists and has all privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Ensure user_0d_2 exists and has SELECT, INSERT privileges on database user_2_db
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT, INSERT ON `user_2_db`.* TO 'user_0d_2'@'localhost';

-- Show privileges for both users
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
