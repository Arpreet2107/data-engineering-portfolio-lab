-- =========================================================
-- 🚀 COMPLETE SQL FUNCTIONS GUIDE (BEGINNER → ADVANCED)
-- =========================================================

-- =========================================================
-- 📌 WHAT IS A FUNCTION?
-- =========================================================

-- 🧠 Definition:
-- A FUNCTION is a reusable SQL block
-- that TAKES input, PROCESSES it,
-- and RETURNS a SINGLE value.

-- Think of it like:
-- ✅ A mini calculator inside SQL
-- ✅ Reusable business logic
-- ✅ Custom built-in function

-- =========================================================
-- 📌 REAL LIFE ANALOGY
-- =========================================================

-- Imagine:

-- square_it(5)

-- INPUT  → 5
-- PROCESS → 5 * 5
-- OUTPUT → 25

-- Function behaves exactly like mathematical functions.

-- =========================================================
-- 📌 WHY FUNCTIONS ARE USED?
-- =========================================================

-- ✅ Reusability
-- Write logic once → use everywhere

-- ✅ Cleaner Queries
-- Avoid repeating calculations

-- ✅ Business Logic Centralization
-- Tax calculation
-- Discount logic
-- Salary bonus logic

-- ✅ Consistency
-- Same formula used everywhere

-- =========================================================
-- 📌 BASIC FUNCTION SYNTAX
-- =========================================================

/*

DELIMITER //

CREATE FUNCTION function_name(parameters)
RETURNS datatype

BEGIN

    -- logic

    RETURN value;

END //

DELIMITER ;

*/

-- =========================================================
-- 📌 YOUR EXAMPLE (DETAILED BREAKDOWN)
-- =========================================================

DELIMITER //

CREATE FUNCTION square_it(x INT)

RETURNS INT

DETERMINISTIC

BEGIN 

    RETURN x * x;

END //

DELIMITER ;

-- =========================================================
-- 📌 USING FUNCTION
-- =========================================================

SELECT 
    unit_price,
    square_it(unit_price)
FROM dim_product;

-- =========================================================
-- 📌 WHAT HAPPENS INTERNALLY?
-- =========================================================

-- Suppose:

-- unit_price = 10

-- SQL does:
-- square_it(10)

-- returns:
-- 100

-- =========================================================
-- 📌 OUTPUT EXAMPLE
-- =========================================================

/*

unit_price | square_it(unit_price)

10         | 100
20         | 400
30         | 900

*/

-- =========================================================
-- 📌 DETERMINISTIC vs NON-DETERMINISTIC
-- =========================================================

-- DETERMINISTIC
-- Same input → same output

-- Example:
-- square_it(5) = 25 always

-- NON-DETERMINISTIC
-- Same input may produce different output

-- Example:
-- NOW()
-- RAND()

-- =========================================================
-- 🔥 SCENARIO 1: TAX CALCULATION FUNCTION
-- =========================================================

-- 🎯 Business Problem:
-- "Calculate 18% GST"

DELIMITER //

CREATE FUNCTION calculate_tax(amount DECIMAL(10,2))

RETURNS DECIMAL(10,2)

DETERMINISTIC

BEGIN

    RETURN amount * 0.18;

END //

DELIMITER ;

-- =========================================================
-- 📌 EXECUTION
-- =========================================================

SELECT 
    amount,
    calculate_tax(amount) AS tax
FROM orders;

-- =========================================================
-- 🔥 SCENARIO 2: FINAL PRICE AFTER DISCOUNT
-- =========================================================

-- 🎯 Business Problem:
-- "Apply 10% discount"

DELIMITER //

CREATE FUNCTION discounted_price(price DECIMAL(10,2))

RETURNS DECIMAL(10,2)

DETERMINISTIC

BEGIN

    RETURN price - (price * 0.10);

END //

DELIMITER ;

-- =========================================================
-- 📌 EXECUTION
-- =========================================================

SELECT 
    unit_price,
    discounted_price(unit_price) AS final_price
FROM dim_product;

-- =========================================================
-- 🔥 SCENARIO 3: CUSTOMER CATEGORY FUNCTION
-- =========================================================

-- 🎯 Business Problem:
-- "Categorize customers by spending"

DELIMITER //

CREATE FUNCTION customer_category(total_spent INT)

RETURNS VARCHAR(50)

DETERMINISTIC

BEGIN

    DECLARE category VARCHAR(50);

    IF total_spent < 1000 THEN
    
        SET category = 'LOW';
        
    ELSEIF total_spent BETWEEN 1000 AND 5000 THEN
    
        SET category = 'MEDIUM';
        
    ELSE
    
        SET category = 'HIGH';
        
    END IF;

    RETURN category;

END //

DELIMITER ;

-- =========================================================
-- 📌 EXECUTION
-- =========================================================

SELECT 
    customer_id,
    total_spent,
    customer_category(total_spent)
FROM customer_summary;

-- =========================================================
-- 🔥 SCENARIO 4: PROFIT FUNCTION
-- =========================================================

-- 🎯 Business Problem:
-- "Calculate profit"

DELIMITER //

CREATE FUNCTION calculate_profit
(
    selling_price DECIMAL(10,2),
    cost_price DECIMAL(10,2)
)

RETURNS DECIMAL(10,2)

DETERMINISTIC

BEGIN

    RETURN selling_price - cost_price;

END //

DELIMITER ;

-- =========================================================
-- 📌 EXECUTION
-- =========================================================

SELECT 
    product_name,
    selling_price,
    cost_price,
    
    calculate_profit(selling_price, cost_price) AS profit

FROM products;

-- =========================================================
-- 📌 WHERE FUNCTIONS ARE USED IN REAL WORLD
-- =========================================================

-- 🛒 E-Commerce
-- Discount calculation

-- 🏦 Banking
-- Interest calculation

-- 📊 Dashboards
-- KPI formulas

-- 🧹 ETL Pipelines
-- Data transformations

-- 👨‍💼 HR Systems
-- Salary/bonus calculations

-- =========================================================
-- 📌 IMPORTANT COMMANDS
-- =========================================================

-- Show all functions
SHOW FUNCTION STATUS;

-- Show function code
SHOW CREATE FUNCTION square_it;

-- Delete function
DROP FUNCTION square_it;

-- =========================================================
-- 📌 LIMITATIONS OF FUNCTIONS
-- =========================================================

-- ❌ Cannot return multiple result sets
-- ❌ Cannot use COMMIT/ROLLBACK
-- ❌ Limited compared to procedures

-- =========================================================
-- 🚀 FINAL SUMMARY
-- =========================================================

-- ✅ Functions = reusable calculation logic
-- ✅ Take input → process → return one value
-- ✅ Used inside SELECT queries
-- ✅ Improve consistency & maintainability
-- ✅ Important for analytics & transformations
-- ✅ Widely used in enterprise SQL systems