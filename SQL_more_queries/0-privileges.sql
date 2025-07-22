-- main_0_0.sql
-- This script ensures that the users 'user_0d_1' and 'user_0d_2' do not exist on localhost.
-- This is necessary to produce the "There is no such grant defined for user ..." error when checking privileges.

DROP USER IF EXISTS 'user_0d_1'@'localhost';
DROP USER IF EXISTS 'user_0d_2'@'localhost';
