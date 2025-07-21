-- This script creates two users and grants them the required privileges

-- Create user_0d_1 and grant all privileges (root user)
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Create user_0d_2 and grant SELECT, INSERT on user_2_db only
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';
