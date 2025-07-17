-- 0-privileges.sql: List all privileges of MySQL users user_0d_1 and user_0d_2 on localhost.
-- If the users do not exist, they are created (without any extra privileges) to avoid errors.

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
