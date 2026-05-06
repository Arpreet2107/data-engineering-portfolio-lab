-- ============================================
-- 🧠 SCENARIO 1: TOP N PRODUCTS PER CATEGORY
-- ============================================

-- 🎯 Business Problem:
-- "Find the TOP 5 most expensive products in EACH category"
-- Used in:
-- - E-commerce dashboards
-- - Product recommendations
-- - Inventory prioritization

SELECT *
FROM
(
    SELECT 
        *,
        
        -- DENSE_RANK assigns rank WITHOUT gaps
        -- PARTITION BY → resets ranking per category
        -- ORDER BY → highest price gets rank 1
        
        DENSE_RANK() OVER(
            PARTITION BY category 
            ORDER BY unit_price DESC
        ) AS ranking
        
    FROM dim_product
) subquery

-- Filter only Top 5 per category
WHERE ranking <= 5;

-- 🧠 Why DENSE_RANK?
-- If prices are same → same rank (no gaps)
-- Example:
-- 1000 → rank 1
-- 1000 → rank 1
-- 900  → rank 2 (NOT 3)



-- ============================================
-- 🧠 SCENARIO 2: REMOVE DUPLICATES (DATA CLEANING)
-- ============================================

-- 🎯 Business Problem:
-- "Keep only ONE record per customer (latest or first)"
-- Used in:
-- - Data cleaning pipelines
-- - ETL jobs
-- - Removing duplicate entries from raw data

SELECT *
FROM
(
    SELECT 
        *,
        
        -- ROW_NUMBER gives UNIQUE numbering
        -- Even if duplicates exist
        
        ROW_NUMBER() OVER(
            PARTITION BY id 
            ORDER BY created_at DESC   -- keep latest record
        ) AS dedup
        
    FROM customers
) subquery

-- Keep only first row per id
WHERE dedup = 1;

-- 🧠 Why ROW_NUMBER?
-- It guarantees ONLY ONE row survives

-- ⚠️ Important:
-- ORDER BY decides WHICH duplicate you keep
-- (latest, oldest, highest value, etc)



-- ============================================
-- 🧠 SCENARIO 3: LAG & LEAD (TIME ANALYSIS)
-- ============================================

-- 🎯 Business Problem:
-- "Compare today's value with previous & next days"
-- Used in:
-- - Weather analysis
-- - Stock market trends
-- - Sales growth tracking

SELECT 
    *,
    
    -- Previous day temperature
    LAG(temp, 1, 0) OVER(ORDER BY date) AS prev_day_temp,
    
    -- 2 days before
    LAG(temp, 2, 0) OVER(ORDER BY date) AS prev_2days_temp,
    
    -- Next day temperature
    LEAD(temp, 1, 0) OVER(ORDER BY date) AS next_day_temp

FROM weather;

-- 🧠 Default value (0) used when no previous/next row exists



-- ============================================
-- 🔥 SCENARIO 4: RUNNING TOTAL (CUMULATIVE SALES)
-- ============================================

-- 🎯 Business Problem:
-- "Calculate total sales till each day"
-- Used in:
-- - Revenue dashboards
-- - KPI tracking

SELECT 
    date,
    sales,
    
    SUM(sales) OVER(
        ORDER BY date
    ) AS running_total

FROM sales_data;

-- 🧠 Each row accumulates previous values



-- ============================================
-- 🔥 SCENARIO 5: MONTHLY SALES PER CUSTOMER
-- ============================================

-- 🎯 Business Problem:
-- "Track customer spending per month"

SELECT 
    customer_id,
    MONTH(order_date) AS month,
    SUM(amount) AS total_spent
    
FROM orders

GROUP BY customer_id, MONTH(order_date);



-- ============================================
-- 🔥 SCENARIO 6: RANK CUSTOMERS BY SPENDING
-- ============================================

-- 🎯 Business Problem:
-- "Find top customers (VIP customers)"

SELECT *
FROM
(
    SELECT 
        customer_id,
        SUM(amount) AS total_spent,
        
        RANK() OVER(
            ORDER BY SUM(amount) DESC
        ) AS rank_position
        
    FROM orders
    GROUP BY customer_id
) subquery

WHERE rank_position <= 10;

-- 🧠 Used in loyalty programs



-- ============================================
-- 🔥 SCENARIO 7: FIND GROWTH (DAY-TO-DAY CHANGE)
-- ============================================

-- 🎯 Business Problem:
-- "Find increase/decrease in sales"

SELECT 
    date,
    sales,
    
    LAG(sales) OVER(ORDER BY date) AS prev_sales,
    
    -- Growth calculation
    sales - LAG(sales) OVER(ORDER BY date) AS daily_growth

FROM sales_data;

-- 🧠 Positive → growth
-- Negative → decline



-- ============================================
-- 🔥 SCENARIO 8: FIRST & LAST PURCHASE
-- ============================================

-- 🎯 Business Problem:
-- "Find customer's first and last order"

SELECT 
    customer_id,
    
    MIN(order_date) AS first_order,
    MAX(order_date) AS last_order

FROM orders

GROUP BY customer_id;



-- ============================================
-- 🔥 SCENARIO 9: GAP BETWEEN EVENTS
-- ============================================

-- 🎯 Business Problem:
-- "Find days between purchases"

SELECT 
    customer_id,
    order_date,
    
    LAG(order_date) OVER(
        PARTITION BY customer_id 
        ORDER BY order_date
    ) AS prev_order_date,
    
    DATEDIFF(
        order_date,
        LAG(order_date) OVER(
            PARTITION BY customer_id 
            ORDER BY order_date
        )
    ) AS days_between

FROM orders;



-- ============================================
-- 🔥 SCENARIO 10: TOP 1 PER GROUP (VERY COMMON)
-- ============================================

-- 🎯 Business Problem:
-- "Find highest paid employee per department"

SELECT *
FROM
(
    SELECT 
        *,
        ROW_NUMBER() OVER(
            PARTITION BY department 
            ORDER BY salary DESC
        ) AS rn
    FROM employees
) subquery

WHERE rn = 1;

-- ============================================
-- 🔥 SCENARIO 11: PERCENTAGE CONTRIBUTION
-- ============================================

-- 🎯 Business Problem:
-- "What % of total revenue does each product contribute?"

SELECT 
    product_id,
    SUM(amount) AS product_revenue,

    -- Total revenue across ALL rows
    SUM(SUM(amount)) OVER() AS total_revenue,

    -- Percentage contribution
    ROUND(
        (SUM(amount) * 100.0) / SUM(SUM(amount)) OVER(), 
        2
    ) AS contribution_percent

FROM orders
GROUP BY product_id;

-- 🧠 Used in:
-- - Revenue breakdown dashboards
-- - Identifying top-performing products



-- ============================================
-- 🔥 SCENARIO 12: MOVING AVERAGE (SMOOTHING)
-- ============================================

-- 🎯 Business Problem:
-- "Find 3-day moving average of sales"

SELECT 
    date,
    sales,

    -- Rolling window of 3 days
    AVG(sales) OVER(
        ORDER BY date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_avg_3days

FROM sales_data;

-- 🧠 Used in:
-- - Trend smoothing
-- - Forecasting
-- - Stock/crypto analysis



-- ============================================
-- 🔥 SCENARIO 13: CUMULATIVE PERCENTAGE (PARETO)
-- ============================================

-- 🎯 Business Problem:
-- "Find top 80% revenue contributors (Pareto 80/20)"

SELECT 
    product_id,
    revenue,

    SUM(revenue) OVER(ORDER BY revenue DESC) AS cumulative_revenue,

    SUM(revenue) OVER() AS total_revenue,

    ROUND(
        SUM(revenue) OVER(ORDER BY revenue DESC) * 100.0
        / SUM(revenue) OVER(),
        2
    ) AS cumulative_percent

FROM product_revenue;

-- 🧠 Used in:
-- - Identify key products/customers driving business



-- ============================================
-- 🔥 SCENARIO 14: SESSIONIZATION (USER BEHAVIOR)
-- ============================================

-- 🎯 Business Problem:
-- "Group user actions into sessions (30 min inactivity break)"

SELECT 
    user_id,
    event_time,

    -- Compare current event with previous event
    CASE 
        WHEN TIMESTAMPDIFF(
            MINUTE,
            LAG(event_time) OVER(PARTITION BY user_id ORDER BY event_time),
            event_time
        ) > 30 THEN 1
        ELSE 0
    END AS new_session_flag

FROM user_events;

-- 🧠 Used in:
-- - Web analytics
-- - User journey tracking



-- ============================================
-- 🔥 SCENARIO 15: FIND MISSING DATES
-- ============================================

-- 🎯 Business Problem:
-- "Detect gaps in daily data (missing records)"

SELECT 
    date,
    LAG(date) OVER(ORDER BY date) AS prev_date,

    DATEDIFF(date, LAG(date) OVER(ORDER BY date)) AS gap

FROM sales_data;

-- 🧠 If gap > 1 → missing data exists



-- ============================================
-- 🔥 SCENARIO 16: NTH HIGHEST SALARY
-- ============================================

-- 🎯 Business Problem:
-- "Find 3rd highest salary"

SELECT *
FROM
(
    SELECT 
        employee_id,
        salary,
        DENSE_RANK() OVER(ORDER BY salary DESC) AS rnk
    FROM employees
) subquery

WHERE rnk = 3;

-- 🧠 Classic interview + real payroll analytics



-- ============================================
-- 🔥 SCENARIO 17: BUCKETING (SEGMENTATION)
-- ============================================

-- 🎯 Business Problem:
-- "Group customers into spending buckets"

SELECT 
    customer_id,
    total_spent,

    CASE 
        WHEN total_spent < 1000 THEN 'Low'
        WHEN total_spent BETWEEN 1000 AND 5000 THEN 'Medium'
        ELSE 'High'
    END AS customer_segment

FROM customer_summary;

-- 🧠 Used in:
-- - Marketing segmentation
-- - Targeted campaigns



-- ============================================
-- 🔥 SCENARIO 18: RETENTION (RETURNING USERS)
-- ============================================

-- 🎯 Business Problem:
-- "Check if customer returned next day"

SELECT 
    customer_id,
    order_date,

    LEAD(order_date) OVER(
        PARTITION BY customer_id 
        ORDER BY order_date
    ) AS next_order,

    CASE 
        WHEN DATEDIFF(
            LEAD(order_date) OVER(
                PARTITION BY customer_id 
                ORDER BY order_date
            ),
            order_date
        ) = 1 THEN 'Retained'
        ELSE 'Not Retained'
    END AS retention_status

FROM orders;

-- 🧠 Core metric in product analytics



-- ============================================
-- 🔥 SCENARIO 19: TOP SELLING PRODUCT PER DAY
-- ============================================

-- 🎯 Business Problem:
-- "Find best product each day"

SELECT *
FROM
(
    SELECT 
        date,
        product_id,
        SUM(quantity) AS total_qty,

        ROW_NUMBER() OVER(
            PARTITION BY date 
            ORDER BY SUM(quantity) DESC
        ) AS rn

    FROM sales
    GROUP BY date, product_id
) subquery

WHERE rn = 1;



-- ============================================
-- 🔥 SCENARIO 20: CHANGE DETECTION
-- ============================================

-- 🎯 Business Problem:
-- "Detect when a value changes (status tracking)"

SELECT 
    user_id,
    status,

    LAG(status) OVER(
        PARTITION BY user_id 
        ORDER BY update_time
    ) AS prev_status,

    CASE 
        WHEN status != LAG(status) OVER(
            PARTITION BY user_id 
            ORDER BY update_time
        )
        THEN 'Changed'
        ELSE 'Same'
    END AS change_flag

FROM user_status_log;

-- 🧠 Used in:
-- - Fraud detection
-- - System monitoring