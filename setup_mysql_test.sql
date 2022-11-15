-- SQL script that sets up the MySQL server for the project
-- It creates a database and a user, granting select privileges on performance_schema
-- Shouldn't fail if either database or user already exists
CREATE DATABASE IF NOT EXISTS happy_pup_db;
CREATE USER IF NOT EXISTS 'hpup_test'@'localhost' IDENTIFIED BY 'hpup_test_pwd';
GRANT ALL PRIVILEGES ON happy_pup_db.* TO 'hpup_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hpup_test'@'localhost';
