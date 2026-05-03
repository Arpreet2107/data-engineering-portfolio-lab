-- ============================================
-- 📌 SQL TRANSFORMATIONS (DATA MANIPULATION & CLEANING)
-- ============================================

-- These transformations are heavily used in:
-- ✔ Data Engineering (ETL pipelines)
-- ✔ Data Cleaning
-- ✔ Feature Engineering
-- ✔ Analytics

-- ============================================
-- 🔢 NUMERIC TRANSFORMATIONS
-- ============================================

SELECT 
    unit_price,

    -- Basic arithmetic
    unit_price * 0.90 AS discounted_price,      -- Apply 10% discount
    unit_price + 10 AS taxed_price,             -- Add fixed tax
    unit_price / 10 AS fractioned_price,        -- Divide value
    unit_price * unit_price AS squared_price,   -- Square value

    -- Rounding
    ROUND(unit_price, 1) AS rounded_price,      -- Round to 1 decimal
    CEIL(unit_price) AS ceil_price,             -- Round up
    FLOOR(unit_price) AS floor_price,           -- Round down

    -- Absolute & power
    ABS(unit_price - 100) AS abs_diff,          -- Absolute difference
    POWER(unit_price, 2) AS power_price,        -- Power function

    -- Modulus
    MOD(unit_price, 2) AS remainder             -- Remainder

FROM dim_product;



-- ============================================
-- 📅 DATE & TIME TRANSFORMATIONS
-- ============================================

-- Current date/time functions
SELECT 
    date,
    NOW() AS current_timestamp,
    CURDATE() AS current_date,
    CURTIME() AS current_time,
    UTC_DATE(),
    UTC_TIME(),
    UTC_TIMESTAMP()
FROM dim_date;


-- Extract parts of date
SELECT 
    date,
    YEAR(date) AS year,
    MONTH(date) AS month,
    DAY(date) AS day,
    WEEK(date) AS week_number,
    WEEKDAY(date) AS weekday_number,
    DAYNAME(date) AS day_name,
    MONTHNAME(date) AS month_name
FROM dim_date;


-- Date calculations
SELECT 
    date,
    DATEDIFF(CURDATE(), date) AS days_difference,
    ADDDATE(date, INTERVAL 5 DAY) AS add_5_days,
    SUBDATE(date, INTERVAL 3 DAY) AS minus_3_days,
    DATE_ADD(date, INTERVAL 1 MONTH) AS next_month,
    DATE_SUB(date, INTERVAL 1 YEAR) AS last_year
FROM dim_date;


-- Date formatting
SELECT 
    date,
    DATE_FORMAT(date, "%W %M %e %Y") AS readable_format,
    DATE_FORMAT(date, "%Y-%m-%d") AS iso_format
FROM dim_date;



-- ============================================
-- 🔄 TYPE CASTING & CONVERSION
-- ============================================

SELECT 
    customer_key,

    -- Convert numeric to string
    CAST(customer_key AS CHAR(100)) AS customer_str,

    -- Convert string to date
    CAST('2025-01-01' AS DATE) AS converted_date,

    -- Convert string to datetime
    CAST('2025-01-01 10:30:00' AS DATETIME) AS converted_datetime

FROM dim_customer;



-- ============================================
-- 🔤 STRING TRANSFORMATIONS
-- ============================================

SELECT 
    first_name,
    last_name,
    email,
    country,

    -- Combine strings
    CONCAT(first_name, ' ', last_name) AS full_name,
    CONCAT_WS(' - ', first_name, last_name, country) AS full_info,

    -- Length
    LENGTH(country) AS country_length,

    -- Case transformations
    LOWER(city) AS city_lower,
    UPPER(country) AS country_upper,

    -- Substring
    SUBSTRING(email, 1, 5) AS email_prefix,
    LEFT(country, 3) AS country_start,
    RIGHT(country, 3) AS country_end,

    -- Replace
    REPLACE(email, '@', '[at]') AS masked_email,

    -- Reverse & repeat
    REVERSE(country) AS reversed_country,
    REPEAT(first_name, 2) AS repeated_name,

    -- Trim spaces
    TRIM('   hello   ') AS trimmed_text,
    LTRIM('   left ') AS left_trim,
    RTRIM(' right   ') AS right_trim

FROM dim_customer;



-- ============================================
-- 🔍 CONDITIONAL TRANSFORMATIONS
-- ============================================

SELECT 
    first_name,
    country,

    -- CASE statement
    CASE 
        WHEN country = 'India' THEN 'Domestic'
        WHEN country = 'USA' THEN 'International'
        ELSE 'Other'
    END AS customer_type,

    -- IF condition (MySQL)
    IF(country = 'India', 'Local', 'Foreign') AS region_type

FROM dim_customer;



-- ============================================
-- 🔢 NULL HANDLING FUNCTIONS
-- ============================================

SELECT 
    first_name,
    email,

    -- Replace NULL values
    IFNULL(email, 'no_email_provided') AS safe_email,

    -- Alternative
    COALESCE(email, 'no_email', 'fallback_email') AS email_fallback

FROM dim_customer;



-- ============================================
-- 🔗 ADVANCED TRANSFORMATIONS (REAL USE CASE)
-- ============================================

SELECT 
    first_name,
    last_name,
    email,

    -- Extract domain from email
    SUBSTRING_INDEX(email, '@', -1) AS email_domain,

    -- Mask email for privacy
    CONCAT(LEFT(email, 3), '****@', SUBSTRING_INDEX(email, '@', -1)) AS masked_email,

    -- Generate username
    LOWER(CONCAT(first_name, '.', last_name)) AS username

FROM dim_customer;



-- ============================================
-- 📊 WINDOW-STYLE PREP (PREVIEW FOR NEXT LEVEL)
-- ============================================

SELECT 
    product_name,
    unit_price,

    -- Ranking logic preview
    CASE 
        WHEN unit_price > 1000 THEN 'Premium'
        WHEN unit_price BETWEEN 500 AND 1000 THEN 'Mid-range'
        ELSE 'Budget'
    END AS price_category

FROM dim_product;



-- ============================================
-- ✅ END OF TRANSFORMATIONS
-- ============================================ 