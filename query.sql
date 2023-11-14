WITH date_range (start_date) AS (
    SELECT '2021-01-01'
    UNION ALL
    SELECT DATE(start_date, '+1 day') 
    FROM date_range
    WHERE start_date < '2021-12-31' 
),
Categories AS (
    SELECT 'Furniture' AS Category, 'Furnishings' AS "Sub-Category", 24000.00/365 AS Meta
    UNION ALL
    SELECT 'Furniture', 'Bookcases', 36000.00/365
    UNION ALL
    SELECT 'Furniture', 'Chairs', 60000.00/365
    UNION ALL
    SELECT 'Furniture', 'Tables', 51600.00/365
    UNION ALL
    SELECT 'Office Supplies', 'Appliances', 30000.00/365
    UNION ALL
    SELECT 'Office Supplies', 'Art', 9000.00/365
    UNION ALL
    SELECT 'Office Supplies', 'Binders', 60000.00/365
    UNION ALL
    SELECT 'Office Supplies', 'Envelopes', 1200.00/365
    UNION ALL
    SELECT 'Office Supplies', 'Fasteners', 600.00/365
    UNION ALL
    SELECT 'Office Supplies', 'Labels', 3600.00/365
    UNION ALL
    SELECT 'Office Supplies', 'Paper', 21000.00/365
    UNION ALL
    SELECT 'Office Supplies', 'Storage', 48000.00/365
    UNION ALL
    SELECT 'Office Supplies', 'Supplies', 12000.00/365
    UNION ALL
    SELECT 'Technology', 'Accessories', 42000.00/365
    UNION ALL
    SELECT 'Technology', 'Copiers', 51000.00/365
    UNION ALL
    SELECT 'Technology', 'Machines', 30000.00/365
    UNION ALL
    SELECT 'Technology', 'Phones', 120000.00/365
)
SELECT *
FROM date_range
CROSS JOIN Categories C;