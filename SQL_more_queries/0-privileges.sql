-- List privileges for user_0d_1 and user_0d_2 on localhost
-- If a user has no privileges, no error will be thrown, and no grants shown for that user

SHOW GRANTS FOR 'user_0d_1'@'localhost';

SHOW GRANTS FOR 'user_0d_2'@'localhost';
