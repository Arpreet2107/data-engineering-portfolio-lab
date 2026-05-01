--Create database
CREATE DATABASE sales;

--Create table
use sales;
CREATE TABLE stores(
    store_id INT,
    store_name VARCHAR(200)
);

--Insert some records
INSERT INTO stores VALUES (1,"store_xyz"),(2,"store,abc");

-- ALTER COMMAND
ALTER TABLE stores_new
ADD COLUMuN store_city;