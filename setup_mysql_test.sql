-- Creates the database hbnb_test_db if it doesn't exist
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;

-- Creates User hbnb_test if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on hbnb_test_db to hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant select privilege on performance_scheme to hbnb_test
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
