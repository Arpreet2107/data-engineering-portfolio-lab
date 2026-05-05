-- ============================================
-- 📌 COMPLETE CTE (COMMON TABLE EXPRESSIONS) GUIDE
-- ============================================

-- CTE = Temporary named result set
-- Exists only for the duration of the query
-- Improves readability, modularity, debugging

-- Syntax:
-- WITH cte_name AS (subquery)
-- SELECT * FROM cte_name;

-- ============================================
-- 🔹 1. BASIC CTE
-- ============================================

WITH cte_products AS (
    SELECT *
    FROM dim_product
    WHERE unit_price > (SELECT AVG(unit_price) FROM dim_product)
)
SELECT *
FROM cte_products;

-- ✔ Cleaner than subquery
-- ✔ Easy to debug


-- ============================================
-- 🔹 2. MULTIPLE CTEs (CHAINING)
-- ============================================

WITH cte_filtered AS (
    SELECT *
    FROM dim_product
    WHERE unit_price > 100
),
cte_selected AS (
    SELECT *
    FROM cte_filtered
    WHERE category = 'Electronics'
)
SELECT *
FROM cte_selected;

-- ✔ Break complex logic into steps


-- ============================================
-- 🔹 3. CTE WITH AGGREGATION
-- ============================================

WITH category_avg AS (
    SELECT 
        category,
        AVG(unit_price) AS avg_price
    FROM dim_product
    GROUP BY category
)
SELECT *
FROM category_avg
WHERE avg_price > 500;

-- ✔ Pre-compute values


-- ============================================
-- 🔹 4. CTE + JOIN (VERY IMPORTANT)
-- ============================================

WITH category_avg AS (
    SELECT 
        category,
        AVG(unit_price) AS avg_price
    FROM dim_product
    GROUP BY category
)
SELECT 
    p.product_name,
    p.unit_price,
    c.avg_price
FROM dim_product p
JOIN category_avg c
ON p.category = c.category
WHERE p.unit_price > c.avg_price;

-- ✔ Real-world analytics pattern


-- ============================================
-- 🔹 5. CTE WITH WINDOW FUNCTIONS
-- ============================================

WITH ranked_products AS (
    SELECT 
        product_name,
        category,
        unit_price,
        RANK() OVER(PARTITION BY category ORDER BY unit_price DESC) AS rnk
    FROM dim_product
)
SELECT *
FROM ranked_products
WHERE rnk <= 3;

-- ✔ Top-N per category (VERY COMMON)


-- ============================================
-- 🔹 6. RECURSIVE CTE (ADVANCED 🔥)
-- ============================================

-- Example: generate numbers 1 to 5

WITH RECURSIVE numbers AS (
    SELECT 1 AS num
    UNION ALL
    SELECT num + 1
    FROM numbers
    WHERE num < 5
)
SELECT * FROM numbers;

-- ✔ Used for:
-- - Hierarchies (org charts)
-- - Tree structures
-- - Graph traversal


-- ============================================
-- 🔹 7. CTE FOR DATA CLEANING / TRANSFORMATION
-- ============================================

WITH cleaned_data AS (
    SELECT 
        product_name,
        LOWER(category) AS category,
        ROUND(unit_price, 2) AS price
    FROM dim_product
)
SELECT *
FROM cleaned_data;

-- ✔ ETL pipelines


-- ============================================
-- 🔹 8. CTE vs SUBQUERY
-- ============================================

-- Subquery (hard to read)
SELECT *
FROM dim_product
WHERE unit_price > (
    SELECT AVG(unit_price)
    FROM dim_product
);

-- CTE (clean & modular)
WITH avg_price AS (
    SELECT AVG(unit_price) AS avg_val
    FROM dim_product
)
SELECT *
FROM dim_product, avg_price
WHERE unit_price > avg_val;

-- ✔ Prefer CTE for readability


-- ============================================
-- 🔹 9. MULTI-STEP PIPELINE (REAL-WORLD 🔥)
-- ============================================

WITH step1 AS (
    SELECT * FROM dim_product WHERE unit_price > 100
),
step2 AS (
    SELECT *, unit_price * 0.9 AS discounted_price FROM step1
),
step3 AS (
    SELECT * FROM step2 WHERE discounted_price > 200
)
SELECT *
FROM step3;

-- ✔ Mimics data pipeline


-- ============================================
-- 🔹 10. PERFORMANCE NOTES
-- ============================================

-- ❌ CTE not always faster than subqueries
-- ❌ Sometimes gets materialized (depends on DB)
-- ✅ Great for readability and debugging

-- ============================================
-- ✅ END OF CTEs
-- ============================================