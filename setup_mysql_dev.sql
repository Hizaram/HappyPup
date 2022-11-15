-- SQL script that sets up the MySQL server for the project
-- It creates a database and a user, granting select privileges on performance_schema
-- Shouldn't fail if either database or user already exists
CREATE DATABASE IF NOT EXISTS happy_pup_db;
CREATE USER IF NOT EXISTS 'hpup_dev'@'localhost' IDENTIFIED BY 'hpup_dev_pwd';
GRANT ALL PRIVILEGES ON happy_pup_db.* TO 'hpup_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hpup_dev'@'localhost';
