-- 6-states.sql
-- Creates the database hbtn_0d_usa and table states
-- Ensures the database and table are not recreated if they exist

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
