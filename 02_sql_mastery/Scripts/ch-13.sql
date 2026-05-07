-- =========================================================
-- 🚀 COMPLETE STORED PROCEDURE GUIDE (BEGINNER → ADVANCED)
-- =========================================================

-- =========================================================
-- 📌 WHAT IS A STORED PROCEDURE?
-- =========================================================

-- 🧠 Definition:
-- A STORED PROCEDURE is a PRE-WRITTEN SQL program
-- stored inside the database.

-- Think of it like:
-- ✅ A reusable SQL function
-- ✅ A mini backend logic layer inside SQL
-- ✅ A stored set of instructions

-- Instead of writing same query again & again:
-- We STORE it once and CALL it whenever needed.

-- =========================================================
-- 🔥 WHY STORED PROCEDURES ARE USED?
-- =========================================================

-- ✅ Reusability
-- Write once → use many times

-- ✅ Performance
-- SQL engine can optimize execution

-- ✅ Security
-- Users can execute procedure without accessing tables directly

-- ✅ Business Logic
-- Complex workflows can be centralized

-- ✅ Cleaner Applications
-- Backend sends CALL procedure instead of huge SQL query

-- =========================================================
-- 📌 BASIC SYNTAX
-- =========================================================

/*

DELIMITER //

CREATE PROCEDURE procedure_name(parameters)
BEGIN

    -- SQL statements

END //

DELIMITER ;

*/

-- =========================================================
-- 📌 WHY DELIMITER IS USED?
-- =========================================================

-- Normally SQL ends query using ;

-- But inside procedure:
-- We write MANY SQL statements

-- So MySQL gets confused where procedure ends.

-- Therefore:
-- We temporarily change delimiter

DELIMITER //

-- Now SQL waits for //
-- instead of ;

-- =========================================================
-- 🔥 SCENARIO 1: SIMPLE INSERT PROCEDURE
-- =========================================================

-- 🎯 Business Problem:
-- "Insert new customer using reusable procedure"

CREATE PROCEDURE first_procedure
(
    IN p_id INT,
    IN p_name VARCHAR(100),
    IN p_email VARCHAR(100)
)

BEGIN

    -- Insert values into customers table
    
    INSERT INTO customers(id, name, email)
    VALUES(p_id, p_name, p_email);

END //

DELIMITER ;

-- =========================================================
-- 📌 CALLING PROCEDURE
-- =========================================================

CALL first_procedure
(
    10,
    'Arpreet',
    'arpreet@gmail.com'
);

-- 🧠 What happens?
-- p_id    → 10
-- p_name  → Arpreet
-- p_email → arpreet@gmail.com

-- These values get inserted into table.

-- =========================================================
-- 📌 IN PARAMETER
-- =========================================================

-- IN means:
-- Value comes INTO procedure

-- Example:
-- CALL procedure(10)

-- 10 enters inside parameter variable.

-- =========================================================
-- 🔥 SCENARIO 2: GET CUSTOMER BY ID
-- =========================================================

-- 🎯 Business Problem:
-- "Fetch customer details dynamically"

DELIMITER //

CREATE PROCEDURE get_customer
(
    IN p_customer_id INT
)

BEGIN

    SELECT *
    FROM customers
    WHERE id = p_customer_id;

END //

DELIMITER ;

-- =========================================================
-- 📌 EXECUTION
-- =========================================================

CALL get_customer(5);

-- 🧠 Used in:
-- - Customer profile pages
-- - CRM systems
-- - Search APIs

-- =========================================================
-- 🔥 SCENARIO 3: UPDATE CUSTOMER EMAIL
-- =========================================================

-- 🎯 Business Problem:
-- "Update customer email"

DELIMITER //

CREATE PROCEDURE update_customer_email
(
    IN p_id INT,
    IN p_new_email VARCHAR(100)
)

BEGIN

    UPDATE customers
    
    SET email = p_new_email
    
    WHERE id = p_id;

END //

DELIMITER ;

-- =========================================================
-- 📌 EXECUTION
-- =========================================================

CALL update_customer_email
(
    1,
    'newmail@gmail.com'
);

-- =========================================================
-- 🔥 SCENARIO 4: DELETE CUSTOMER
-- =========================================================

-- 🎯 Business Problem:
-- "Delete customer safely"

DELIMITER //

CREATE PROCEDURE delete_customer
(
    IN p_customer_id INT
)

BEGIN

    DELETE FROM customers
    WHERE id = p_customer_id;

END //

DELIMITER ;

-- =========================================================
-- 📌 EXECUTION
-- =========================================================

CALL delete_customer(3);

-- =========================================================
-- 🔥 SCENARIO 5: TOTAL ORDERS OF CUSTOMER
-- =========================================================

-- 🎯 Business Problem:
-- "Calculate customer total orders"

DELIMITER //

CREATE PROCEDURE customer_total_orders
(
    IN p_customer_id INT
)

BEGIN

    SELECT 
        customer_id,
        COUNT(*) AS total_orders
        
    FROM orders
    
    WHERE customer_id = p_customer_id
    
    GROUP BY customer_id;

END //

DELIMITER ;

-- =========================================================
-- 📌 EXECUTION
-- =========================================================

CALL customer_total_orders(101);

-- =========================================================
-- 🔥 SCENARIO 6: TOTAL REVENUE OF CUSTOMER
-- =========================================================

DELIMITER //

CREATE PROCEDURE customer_total_revenue
(
    IN p_customer_id INT
)

BEGIN

    SELECT 
        customer_id,
        SUM(amount) AS total_revenue
        
    FROM orders
    
    WHERE customer_id = p_customer_id
    
    GROUP BY customer_id;

END //

DELIMITER ;

-- =========================================================
-- 📌 EXECUTION
-- =========================================================

CALL customer_total_revenue(101);

-- =========================================================
-- 🔥 SCENARIO 7: CONDITIONAL LOGIC INSIDE PROCEDURE
-- =========================================================

-- 🎯 Business Problem:
-- "Categorize customer"

DELIMITER //

CREATE PROCEDURE customer_category
(
    IN p_total_spent INT
)

BEGIN

    IF p_total_spent < 1000 THEN
    
        SELECT 'LOW VALUE CUSTOMER' AS category;
        
    ELSEIF p_total_spent BETWEEN 1000 AND 5000 THEN
    
        SELECT 'MEDIUM VALUE CUSTOMER' AS category;
        
    ELSE
    
        SELECT 'HIGH VALUE CUSTOMER' AS category;
        
    END IF;

END //

DELIMITER ;

-- =========================================================
-- 📌 EXECUTION
-- =========================================================

CALL customer_category(7000);

-- =========================================================
-- 🔥 SCENARIO 8: LOOP INSIDE PROCEDURE
-- =========================================================

-- 🎯 Business Problem:
-- "Print numbers from 1 to 5"

DELIMITER //

CREATE PROCEDURE loop_demo()

BEGIN

    DECLARE counter INT DEFAULT 1;

    WHILE counter <= 5 DO
    
        SELECT counter;
        
        SET counter = counter + 1;
        
    END WHILE;

END //

DELIMITER ;

-- =========================================================
-- 📌 EXECUTION
-- =========================================================

CALL loop_demo();

-- =========================================================
-- 🔥 SCENARIO 9: OUT PARAMETER
-- =========================================================

-- 🎯 Business Problem:
-- "Return total customer count"

DELIMITER //

CREATE PROCEDURE total_customers
(
    OUT total INT
)

BEGIN

    SELECT COUNT(*)
    INTO total
    FROM customers;

END //

DELIMITER ;

-- =========================================================
-- 📌 EXECUTION
-- =========================================================

SET @total_customers = 0;

CALL total_customers(@total_customers);

SELECT @total_customers;

-- =========================================================
-- 📌 UNDERSTANDING OUT PARAMETER
-- =========================================================

-- OUT sends value OUTSIDE procedure

-- Procedure calculates value
-- then stores into variable.

-- =========================================================
-- 🔥 SCENARIO 10: INOUT PARAMETER
-- =========================================================

-- 🎯 Business Problem:
-- "Increase bonus amount"

DELIMITER //

CREATE PROCEDURE increment_bonus
(
    INOUT bonus INT
)

BEGIN

    SET bonus = bonus + 1000;

END //

DELIMITER ;

-- =========================================================
-- 📌 EXECUTION
-- =========================================================

SET @emp_bonus = 5000;

CALL increment_bonus(@emp_bonus);

SELECT @emp_bonus;

-- Output:
-- 6000

-- =========================================================
-- 📌 IN vs OUT vs INOUT
-- =========================================================

-- IN
-- Input only

-- OUT
-- Output only

-- INOUT
-- Both input and output

-- =========================================================
-- 🔥 SCENARIO 11: ERROR HANDLING
-- =========================================================

-- 🎯 Business Problem:
-- "Handle SQL exceptions"

DELIMITER //

CREATE PROCEDURE safe_insert
(
    IN p_id INT,
    IN p_name VARCHAR(100)
)

BEGIN

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    
    BEGIN
    
        SELECT 'ERROR OCCURRED' AS message;
        
    END;

    INSERT INTO customers(id, name)
    VALUES(p_id, p_name);

END //

DELIMITER ;

-- =========================================================
-- 🔥 SCENARIO 12: TRANSACTION INSIDE PROCEDURE
-- =========================================================

-- 🎯 Business Problem:
-- "Transfer money between accounts"

DELIMITER //

CREATE PROCEDURE transfer_money
(
    IN sender INT,
    IN receiver INT,
    IN amount INT
)

BEGIN

    START TRANSACTION;

    -- Deduct from sender
    UPDATE accounts
    SET balance = balance - amount
    WHERE id = sender;

    -- Add to receiver
    UPDATE accounts
    SET balance = balance + amount
    WHERE id = receiver;

    COMMIT;

END //

DELIMITER ;

-- 🧠 Why transaction?
-- Either BOTH updates happen
-- OR none happen

-- Prevents inconsistent data

-- =========================================================
-- 🔥 SCENARIO 13: PROCEDURE + CURSOR
-- =========================================================

-- 🎯 Business Problem:
-- "Process rows one-by-one"

-- Cursor = row iterator

DELIMITER //

CREATE PROCEDURE cursor_demo()

BEGIN

    DECLARE done INT DEFAULT FALSE;

    DECLARE c_name VARCHAR(100);

    DECLARE customer_cursor CURSOR FOR
    
        SELECT name FROM customers;

    DECLARE CONTINUE HANDLER FOR NOT FOUND
    SET done = TRUE;

    OPEN customer_cursor;

    read_loop: LOOP

        FETCH customer_cursor INTO c_name;

        IF done THEN
            LEAVE read_loop;
        END IF;

        SELECT c_name;

    END LOOP;

    CLOSE customer_cursor;

END //

DELIMITER ;

-- =========================================================
-- 🔥 SCENARIO 14: DYNAMIC FILTERING
-- =========================================================

-- 🎯 Business Problem:
-- "Find orders above dynamic amount"

DELIMITER //

CREATE PROCEDURE orders_above_amount
(
    IN p_amount INT
)

BEGIN

    SELECT *
    FROM orders
    WHERE amount > p_amount;

END //

DELIMITER ;

-- =========================================================
-- 📌 EXECUTION
-- =========================================================

CALL orders_above_amount(5000);

-- =========================================================
-- 🔥 SCENARIO 15: AUTOMATED REPORT PROCEDURE
-- =========================================================

-- 🎯 Business Problem:
-- "Generate daily sales report"

DELIMITER //

CREATE PROCEDURE daily_sales_report()

BEGIN

    SELECT 
        order_date,
        COUNT(*) AS total_orders,
        SUM(amount) AS total_sales,
        AVG(amount) AS avg_sales
        
    FROM orders
    
    GROUP BY order_date;

END //

DELIMITER ;

-- =========================================================
-- 📌 HOW COMPANIES USE STORED PROCEDURES
-- =========================================================

-- Backend Application
--        ↓
-- CALL procedure_name()
--        ↓
-- Database executes business logic
--        ↓
-- Result returned

-- =========================================================
-- 📌 REAL-WORLD USE CASES
-- =========================================================

-- 🏦 Banking Systems
-- Money transfers

-- 🛒 E-Commerce
-- Order placement

-- 📊 Dashboards
-- Prebuilt reports

-- 🧹 ETL Pipelines
-- Data cleaning

-- 🔐 Security
-- Controlled database access

-- =========================================================
-- 📌 IMPORTANT COMMANDS
-- =========================================================

-- Show all procedures
SHOW PROCEDURE STATUS;

-- Show procedure code
SHOW CREATE PROCEDURE first_procedure;

-- Delete procedure
DROP PROCEDURE first_procedure;

-- =========================================================
-- 📌 STORED PROCEDURE vs FUNCTION
-- =========================================================

-- PROCEDURE
-- Can return multiple values
-- Uses CALL

-- FUNCTION
-- Must return one value
-- Used inside SELECT

-- =========================================================
-- 🚀 FINAL SUMMARY
-- =========================================================

-- ✅ Stored Procedures = reusable SQL programs
-- ✅ Used heavily in enterprise systems
-- ✅ Support conditions, loops, transactions, cursors
-- ✅ Improve security & maintainability
-- ✅ Centralize business logic
-- ✅ Important for Data Engineering + Backend Systems