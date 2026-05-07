-- ============================================
-- 🧠 SCENARIO 1: DEDUPLICATION USING VIEW
-- ============================================

-- 🎯 Business Problem:
-- "Create a clean customer dataset with NO duplicates"
-- This will be reused across dashboards, ETL pipelines, etc.

CREATE VIEW dedup_view AS

-- This is the query stored inside the view
SELECT 
    subquery.*
FROM 
(
    SELECT 
        *,
        
        -- Assign row numbers per customer ID
        -- PARTITION BY id → groups rows by customer
        -- ORDER BY id → determines which record gets priority
        
        ROW_NUMBER() OVER (
            PARTITION BY id 
            ORDER BY id
        ) AS dedup
        
    FROM customers
) subquery

-- Keep only the FIRST row per customer
WHERE dedup = 1;

-- ============================================
-- 🔥 SCENARIO 2: TOP CUSTOMERS VIEW
-- ============================================

-- 🎯 Business Problem:
-- "Create reusable view for top customers by revenue"

CREATE VIEW top_customers AS

SELECT *
FROM
(
    SELECT 
        customer_id,
        SUM(amount) AS total_spent,

        -- Rank customers by spending
        RANK() OVER(ORDER BY SUM(amount) DESC) AS rnk

    FROM orders
    GROUP BY customer_id
) subquery

-- Keep only top 10 customers
WHERE rnk <= 10;

-- 👉 Now any team can query:
-- SELECT * FROM top_customers;

-- ============================================
-- 🔥 SCENARIO 3: DAILY SALES SUMMARY VIEW
-- ============================================

-- 🎯 Business Problem:
-- "Provide ready-to-use daily sales dashboard data"

CREATE VIEW daily_sales_summary AS

SELECT 
    date,
    SUM(sales) AS total_sales,
    
    -- Running total
    SUM(SUM(sales)) OVER(ORDER BY date) AS running_total

FROM sales_data
GROUP BY date;

-- 👉 Used directly in BI tools like Power BI / Tableau

-- ============================================
-- 🔥 SCENARIO 4: CUSTOMER SEGMENT VIEW
-- ============================================

-- 🎯 Business Problem:
-- "Categorize customers based on spending"

CREATE VIEW customer_segments AS

SELECT 
    customer_id,
    SUM(amount) AS total_spent,

    CASE 
        WHEN SUM(amount) < 1000 THEN 'Low'
        WHEN SUM(amount) BETWEEN 1000 AND 5000 THEN 'Medium'
        ELSE 'High'
    END AS segment

FROM orders
GROUP BY customer_id;

-- 👉 Marketing team can directly use this

-- ============================================
-- 🔥 SCENARIO 5: RECENT ACTIVITY VIEW
-- ============================================

-- 🎯 Business Problem:
-- "Get latest activity per user"

CREATE VIEW latest_user_activity AS

SELECT *
FROM
(
    SELECT 
        user_id,
        event_time,
        
        ROW_NUMBER() OVER(
            PARTITION BY user_id 
            ORDER BY event_time DESC
        ) AS rn

    FROM user_events
) subquery

WHERE rn = 1;

-- 👉 Useful for dashboards & monitoring

-- ============================================
-- 🔥 SCENARIO 6: SALES GROWTH VIEW
-- ============================================

-- 🎯 Business Problem:
-- "Track day-to-day growth"

CREATE VIEW sales_growth AS

SELECT 
    date,
    sales,

    LAG(sales) OVER(ORDER BY date) AS prev_sales,

    sales - LAG(sales) OVER(ORDER BY date) AS growth

FROM sales_data;

-- 👉 Used for KPI dashboards

-- ============================================
-- 🔥 SCENARIO 7: ACTIVE CUSTOMERS VIEW
-- ============================================

-- 🎯 Business Problem:
-- "Get customers who made a purchase in last 30 days"

CREATE VIEW active_customers AS

SELECT DISTINCT customer_id
FROM orders
WHERE order_date >= CURRENT_DATE - INTERVAL 30 DAY;

-- 🧠 Used in:
-- - Retargeting campaigns
-- - Active user dashboards

-- ============================================
-- 🔥 SCENARIO 8: INACTIVE CUSTOMERS VIEW
-- ============================================

-- 🎯 Business Problem:
-- "Find customers who have NOT ordered recently"

CREATE VIEW inactive_customers AS

SELECT c.customer_id
FROM customers c
LEFT JOIN orders o 
    ON c.customer_id = o.customer_id
    AND o.order_date >= CURRENT_DATE - INTERVAL 30 DAY
WHERE o.customer_id IS NULL;

-- 🧠 Used for:
-- - Win-back campaigns

-- ============================================
-- 🔥 SCENARIO 9: HIGH VALUE ORDERS VIEW
-- ============================================

-- 🎯 Business Problem:
-- "Filter high-value transactions"

CREATE VIEW high_value_orders AS

SELECT *
FROM orders
WHERE amount > 10000;

-- 🧠 Used in:
-- - Fraud detection
-- - VIP customer analysis
-- ============================================
-- 🔥 SCENARIO 10: PRODUCT PERFORMANCE VIEW
-- ============================================

-- 🎯 Business Problem:
-- "Track product sales and revenue"

CREATE VIEW product_performance AS

SELECT 
    product_id,
    COUNT(*) AS total_orders,
    SUM(amount) AS total_revenue,
    AVG(amount) AS avg_order_value

FROM orders
GROUP BY product_id;

-- 🧠 Used in:
-- - Inventory decisions
-- - Product ranking
-- ============================================
-- 🔥 SCENARIO 11: CUSTOMER LIFETIME VALUE (CLV)
-- ============================================

-- 🎯 Business Problem:
-- "Calculate total revenue per customer"

CREATE VIEW customer_clv AS

SELECT 
    customer_id,
    SUM(amount) AS lifetime_value

FROM orders
GROUP BY customer_id;

-- 🧠 Used in:
-- - Marketing spend optimization
-- ============================================
-- 🔥 SCENARIO 12: REPEAT CUSTOMERS VIEW
-- ============================================

-- 🎯 Business Problem:
-- "Find customers who ordered more than once"

CREATE VIEW repeat_customers AS

SELECT customer_id
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 1;

-- 🧠 Used in:
-- - Retention analysis
-- ============================================
-- 🔥 SCENARIO 13: FIRST PURCHASE VIEW
-- ============================================

-- 🎯 Business Problem:
-- "Find first order of each customer"

CREATE VIEW first_purchase AS

SELECT 
    customer_id,
    MIN(order_date) AS first_order

FROM orders
GROUP BY customer_id;

-- 🧠 Used in:
-- - Cohort analysis
-- ============================================
-- 🔥 SCENARIO 14: LAST PURCHASE VIEW
-- ============================================

CREATE VIEW last_purchase AS

SELECT 
    customer_id,
    MAX(order_date) AS last_order

FROM orders
GROUP BY customer_id;

-- 🧠 Used in:
-- - Recency tracking
-- ============================================
-- 🔥 SCENARIO 15: DAILY ORDER COUNT VIEW
-- ============================================

CREATE VIEW daily_orders AS

SELECT 
    date,
    COUNT(*) AS total_orders

FROM orders
GROUP BY date;

-- 🧠 Used in:
-- - Daily dashboards
-- ============================================
-- 🔥 SCENARIO 16: WEEKLY SALES VIEW
-- ============================================

CREATE VIEW weekly_sales AS

SELECT 
    WEEK(order_date) AS week,
    SUM(amount) AS total_sales

FROM orders
GROUP BY WEEK(order_date);

-- 🧠 Used in:
-- - Weekly reporting
-- ============================================
-- 🔥 SCENARIO 17: PRODUCT STOCK ALERT VIEW
-- ============================================

-- 🎯 Business Problem:
-- "Find low stock products"

CREATE VIEW low_stock_products AS

SELECT *
FROM products
WHERE stock_quantity < 10;

-- 🧠 Used in:
-- - Inventory alerts
-- ============================================
-- 🔥 SCENARIO 18: CUSTOMER ORDER FREQUENCY
-- ============================================

CREATE VIEW customer_frequency AS

SELECT 
    customer_id,
    COUNT(*) AS order_count

FROM orders
GROUP BY customer_id;

-- 🧠 Used in:
-- - Behavioral segmentation
-- ============================================
-- 🔥 SCENARIO 19: SALES BY REGION
-- ============================================

CREATE VIEW sales_by_region AS

SELECT 
    region,
    SUM(amount) AS total_sales

FROM orders
GROUP BY region;

-- 🧠 Used in:
-- - Geo analytics
-- ============================================
-- 🔥 SCENARIO 20: CANCELLED ORDERS VIEW
-- ============================================

CREATE VIEW cancelled_orders AS

SELECT *
FROM orders
WHERE status = 'cancelled';

-- 🧠 Used in:
-- - Operations monitoring
-- ============================================
-- 🔥 SCENARIO 21: SUCCESSFUL ORDERS VIEW
-- ============================================

CREATE VIEW successful_orders AS

SELECT *
FROM orders
WHERE status = 'completed';

-- 🧠 Used in:
-- - Revenue tracking