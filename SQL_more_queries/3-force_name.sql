-- 3-force_name.sql
-- Create table force_name with id INT and name VARCHAR(256) NOT NULL
-- The database is passed as an argument when running mysql, so no database name in the script
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
