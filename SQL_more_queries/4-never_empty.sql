-- 4-never_empty.sql
-- Create table id_not_null with id INT NOT NULL default 1 and name VARCHAR(256)
-- The database will be specified when running mysql

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);
