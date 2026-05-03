-- ============================================
-- 📌 DML COMMANDS (Data Manipulation Language)
-- ============================================

-- DML is used to work with data inside tables:
-- INSERT → add data
-- UPDATE → modify data
-- DELETE → remove data
-- SELECT → retrieve data

-- ============================================
-- 🔹 INSERT COMMAND
-- ============================================

-- Insert a single row
INSERT INTO customers (id, name, email, country)
VALUES (1, 'Arpreet', 'arpreet@gmail.com', 'India');

-- Insert multiple rows
INSERT INTO customers (id, name, email, country)
VALUES 
(2, 'Sam', 'sam@gmail.com', 'USA'),
(3, 'John', 'john@gmail.com', 'UK');

-- Insert with partial columns (others will be NULL/default)
INSERT INTO customers (id, name)
VALUES (4, 'Alex');



-- ============================================
-- 🔹 UPDATE COMMAND
-- ============================================

-- Update a specific row using condition
UPDATE customers
SET name = 'Sam Updated'
WHERE email = 'sam@gmail.com';

-- Update multiple columns
UPDATE customers
SET name = 'John Updated', country = 'Canada'
WHERE id = 3;

-- Update multiple rows using condition
UPDATE customers
SET country = 'India'
WHERE country = 'USA';

-- ⚠️ WARNING: This updates ALL rows (avoid unless intended)
-- UPDATE customers
-- SET country = 'Global';



-- ============================================
-- 🔹 DELETE COMMAND
-- ============================================

-- Delete specific row
DELETE FROM customers
WHERE email = 'sam@gmail.com';

-- Delete multiple rows
DELETE FROM customers
WHERE country = 'UK';

-- Delete ALL rows (table structure remains)
-- ⚠️ Use carefully
-- DELETE FROM customers;



-- ============================================
-- 🔹 SELECT COMMAND (READ DATA)
-- ============================================

-- Select all columns
SELECT * FROM customers;

-- Select specific columns
SELECT name, email FROM customers;

-- Select with alias
SELECT name AS customer_name, country AS location
FROM customers;



-- ============================================
-- 🔹 FILTERING (WHERE CLAUSE)
-- ============================================

-- Basic condition
SELECT * FROM customers
WHERE country = 'India';

-- Multiple conditions (AND / OR)
SELECT * FROM customers
WHERE country = 'India' AND name = 'Arpreet';

SELECT * FROM customers
WHERE country = 'India' OR country = 'USA';



-- ============================================
-- 🔹 DISTINCT (UNIQUE VALUES)
-- ============================================

SELECT DISTINCT country FROM customers;



-- ============================================
-- 🔹 LIMIT (RESTRICT OUTPUT)
-- ============================================

SELECT * FROM customers
LIMIT 5;



-- ============================================
-- 🔹 ORDER BY (SORTING)
-- ============================================

-- Ascending order
SELECT * FROM customers
ORDER BY name ASC;

-- Descending order
SELECT * FROM customers
ORDER BY id DESC;



-- ============================================
-- 🔹 LIKE (PATTERN MATCHING)
-- ============================================

-- Names starting with 'A'
SELECT * FROM customers
WHERE name LIKE 'A%';

-- Names ending with 'n'
SELECT * FROM customers
WHERE name LIKE '%n';

-- Names with specific pattern
SELECT * FROM customers
WHERE name LIKE '_a%';



-- ============================================
-- 🔹 IN / NOT IN
-- ============================================

-- Match multiple values
SELECT * FROM customers
WHERE country IN ('India', 'USA');

-- Exclude values
SELECT * FROM customers
WHERE country NOT IN ('UK');



-- ============================================
-- 🔹 BETWEEN
-- ============================================

SELECT * FROM customers
WHERE id BETWEEN 1 AND 3;



-- ============================================
-- 🔹 NULL CHECK
-- ============================================

-- Find NULL values
SELECT * FROM customers
WHERE email IS NULL;

-- Find NOT NULL values
SELECT * FROM customers
WHERE email IS NOT NULL;



-- ============================================
-- 🔹 AGGREGATE FUNCTIONS
-- ============================================

-- Count rows
SELECT COUNT(*) AS total_customers FROM customers;

-- Average (example column required)
-- SELECT AVG(age) FROM customers;

-- Sum (example column required)
-- SELECT SUM(salary) FROM customers;



-- ============================================
-- 🔹 GROUP BY
-- ============================================

-- Count customers per country
SELECT country, COUNT(*) AS total
FROM customers
GROUP BY country;



-- ============================================
-- 🔹 HAVING (FILTER GROUPED DATA)
-- ============================================

SELECT country, COUNT(*) AS total
FROM customers
GROUP BY country
HAVING total > 1;



-- ============================================
-- 🔹 CASE (CONDITIONAL LOGIC)
-- ============================================

SELECT name,
CASE 
    WHEN country = 'India' THEN 'Domestic'
    ELSE 'International'
END AS customer_type
FROM customers;



-- ============================================
-- 🔹 SUBQUERY
-- ============================================

-- Customers who have orders
SELECT * FROM customers
WHERE id IN (
    SELECT cust_id FROM orders
);



-- ============================================
-- 🔹 EXISTS
-- ============================================

SELECT * FROM customers c
WHERE EXISTS (
    SELECT 1 FROM orders o WHERE o.cust_id = c.id
);



-- ============================================
-- ✅ END OF DML COMMANDS
-- ============================================