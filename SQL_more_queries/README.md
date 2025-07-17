-- Create user_0d_1 if not exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';

-- Create user_0d_2 if not exists
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Grant some privileges (optional; only needed if not already done)
-- GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- GRANT SELECT ON *.* TO 'user_0d_2'@'localhost';

-- Show privileges of user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Show privileges of user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
