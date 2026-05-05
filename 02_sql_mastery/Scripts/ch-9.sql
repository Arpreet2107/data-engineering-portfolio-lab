-- ============================================
-- 📌 COMPLETE SQL SUBQUERIES GUIDE
-- ============================================

-- A subquery = query inside another query
-- Used for filtering, comparison, transformation

-- ============================================
-- 🔹 1. SCALAR SUBQUERY (returns single value)
-- ============================================

-- Find products with price above average
SELECT *
FROM dim_product
WHERE unit_price > (
    SELECT AVG(unit_price) 
    FROM dim_product
);

-- ✔ Used with =, >, <, etc.


-- ============================================
-- 🔹 2. MULTI-ROW SUBQUERY
-- ============================================

-- Find products in categories that exist in another condition
SELECT *
FROM dim_product
WHERE category IN (
    SELECT category
    FROM dim_product
    WHERE unit_price > 1000
);

-- ✔ Use IN when subquery returns multiple values


-- ============================================
-- 🔹 3. CORRELATED SUBQUERY (VERY IMPORTANT)
-- ============================================

-- Subquery depends on outer query row

SELECT *
FROM dim_product p1
WHERE unit_price > (
    SELECT AVG(unit_price)
    FROM dim_product p2
    WHERE p1.category = p2.category
);

-- ✔ Runs once per row (costly but powerful)
-- ✔ Used in real analytics


-- ============================================
-- 🔹 4. EXISTS SUBQUERY (VERY IMPORTANT)
-- ============================================

-- Check if related data exists

SELECT *
FROM dim_customer c
WHERE EXISTS (
    SELECT 1
    FROM fact_sales s
    WHERE s.customer_key = c.customer_key
);

-- ✔ Faster than IN in many cases
-- ✔ Stops at first match


-- ============================================
-- 🔹 5. NOT EXISTS
-- ============================================

-- Customers with NO orders

SELECT *
FROM dim_customer c
WHERE NOT EXISTS (
    SELECT 1
    FROM fact_sales s
    WHERE s.customer_key = c.customer_key
);


-- ============================================
-- 🔹 6. ANY / ALL SUBQUERY
-- ============================================

-- ANY: at least one condition true

SELECT *
FROM dim_product
WHERE unit_price > ANY (
    SELECT unit_price
    FROM dim_product
    WHERE category = 'Electronics'
);

-- ALL: must satisfy all values

SELECT *
FROM dim_product
WHERE unit_price > ALL (
    SELECT unit_price
    FROM dim_product
    WHERE category = 'Clothing'
);


-- ============================================
-- 🔹 7. SUBQUERY IN SELECT (DERIVED COLUMN)
-- ============================================

-- Add avg price as column

SELECT 
    product_name,
    unit_price,
    (SELECT AVG(unit_price) FROM dim_product) AS avg_price
FROM dim_product;


-- ============================================
-- 🔹 8. SUBQUERY IN FROM (DERIVED TABLE)
-- ============================================

SELECT *
FROM (
    SELECT category, AVG(unit_price) AS avg_price
    FROM dim_product
    GROUP BY category
) AS category_avg
WHERE avg_price > 500;

-- ✔ Acts like temporary table


-- ============================================
-- 🔹 9. SUBQUERY IN HAVING
-- ============================================

SELECT 
    category,
    AVG(unit_price) AS avg_price
FROM dim_product
GROUP BY category
HAVING AVG(unit_price) > (
    SELECT AVG(unit_price) 
    FROM dim_product
);


-- ============================================
-- 🔹 10. NESTED SUBQUERIES
-- ============================================

SELECT *
FROM dim_product
WHERE category IN (
    SELECT category
    FROM dim_product
    WHERE unit_price > (
        SELECT AVG(unit_price)
        FROM dim_product
    )
);


-- ============================================
-- 🔹 11. TOP-N USING SUBQUERY
-- ============================================

-- Top 3 expensive products

SELECT *
FROM dim_product
WHERE unit_price IN (
    SELECT unit_price
    FROM dim_product
    ORDER BY unit_price DESC
    LIMIT 3
);


-- ============================================
-- 🔹 12. SUBQUERY VS JOIN (IMPORTANT)
-- ============================================

-- Subquery version
SELECT *
FROM dim_customer
WHERE customer_key IN (
    SELECT customer_key FROM fact_sales
);

-- JOIN version (better in most cases)
SELECT DISTINCT c.*
FROM dim_customer c
JOIN fact_sales s
ON c.customer_key = s.customer_key;


-- ============================================
-- 🔹 13. PERFORMANCE NOTES
-- ============================================

-- ❌ Correlated subqueries → slow (O(n^2) sometimes)
-- ✅ EXISTS → optimized
-- ✅ JOIN often better than subqueries

-- ============================================
-- ✅ END OF SUBQUERIES
-- ============================================