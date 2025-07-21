-- 5-unique_id.sql
-- Create table unique_id with id INT default 1 and unique constraint
-- name is VARCHAR(256)
-- Database name will be provided as an argument

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
