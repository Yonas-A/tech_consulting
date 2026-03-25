-- 1. Calculate the total quantity_sold of products in the 'Electronics' category.
SELECT
    SUM(quantity_sold) AS total_electronics_sold
FROM
    sales s
    JOIN products p
WHERE
    p.product_id = s.product_id
    AND p.category = 'Electronics';

-- 2. Retrieve the product_name and total_price from the Sales table, calculating the
-- total_price as quantity_sold multiplied by unit_pric
SELECT
    p.product_name,
    (s.quantity_sold * p.unit_price) AS total_price
FROM
    products p
    JOIN sales s
WHERE
    s.product_id = p.product_id;

-- 3. Identify the Most Frequently Sold Product from Sales table.
SELECT
    p.product_name,
    SUM(s.quantity_sold) AS total_sold
FROM
    products p
    JOIN sales s ON p.product_id = s.product_id
GROUP BY
    p.product_id,
    p.product_name
ORDER BY
    total_sold DESC
LIMIT
    1;

-- 4.  Find the Products Not Sold from Products table.
SELECT
    p.product_id,
    p.product_name,
    p.category,
    p.unit_price
FROM
    Products p
    LEFT JOIN sales s ON p.product_id = s.product_id
WHERE
    s.product_id IS NULL;

-- Filters for products where no matching sales record was found
-- 5. Calculate the total revenue generated from sales for each product category.
SELECT
    p.category,
    SUM(s.total_price) AS total_revenue
FROM
    sales s
    JOIN products p ON p.product_id = s.product_id
GROUP BY
    p.category;

-- 6. Find the product category with the highest average unit price.
SELECT
    category,
    AVG(unit_price)
FROM
    products
GROUP BY
    category
ORDER BY
    AVG(unit_price) DESC
LIMIT
    1;

-- 7. Identify products with total sales exceeding 30.
SELECT
    p.product_id,
    p.product_name,
    p.category,
    SUM(s.quantity_sold) AS total_sold
FROM
    products p
    JOIN sales s ON p.product_id = s.product_id
GROUP BY
    p.product_id
HAVING
    total_sold > 30;

-- 8. Count the number of sales made in each month.
SELECT
    YEAR (s.sale_date),
    MONTH (s.sale_date),
    COUNT(s.quantity_sold)
FROM
    sales s
GROUP BY
    YEAR (s.sale_date),
    MONTH (s.sale_date);

-- 9. Retrieve Sales Details for Products with 'Smart' in Their Name.
SELECT
    s.sale_id,
    s.product_id,
    s.quantity_sold,
    s.total_price
FROM
    sales s
    JOIN products p ON s.product_id = p.product_id
WHERE
    p.product_name LIKE '%smart%';

-- 10. Determine the average quantity sold for products with a unit price greater than $100.
SELECT
    --     p.product_id,
    --     p.product_name,
    AVG(s.quantity_sold) AS avg_quantity_sold
FROM
    products p
    JOIN sales s ON p.product_id = s.product_id
WHERE
    p.unit_price > 100;

-- GROUP BY p.product_id;
-- 11. Retrieve the product name and total sales revenue for each product.
SELECT
    p.product_name,
    SUM(s.total_price)
FROM
    products p
    JOIN sales s ON p.product_id = s.product_id
GROUP BY
    p.product_id;

-- 12. List all sales along with the corresponding product names
SELECT
    s.sale_id,
    s.product_id,
    p.product_name,
    s.quantity_sold,
    s.sale_date,
    s.total_price
FROM
    sales s
    JOIN products p ON s.product_id = p.product_id;

-- 13. Retrieve the product name and total sales revenue for each product.
SELECT
    p.product_name,
    SUM(s.total_price) AS sales_revenue
FROM
    products p
    JOIN sales s ON p.product_id = s.product_id
GROUP BY
    p.product_id;

-- 14. Rank products based on total sales revenue.
SELECT
    product_name,
    product_id,
    total_sales_revenue,
    RANK() OVER (
        ORDER BY
            total_sales_revenue DESC
    ) AS revenue_rank
FROM
    (
        SELECT
            p.product_name,
            p.product_id,
            sum(s.total_price) AS total_sales_revenue
        FROM
            sales s
            JOIN products p ON s.product_id = p.product_id
        GROUP BY
            p.product_id
    ) temp;

SELECT
    product_name,
    total_sales_revenue,
    RANK() OVER (
        ORDER BY
            total_sales_revenue DESC
    ) AS revenue_rank
FROM
    (
        SELECT
            p.product_name,
            SUM(s.total_price) AS total_sales_revenue
        FROM
            Sales s
            JOIN Products p ON p.product_id = s.product_id
        GROUP BY
            p.product_id,
            p.product_name
    ) t;

-- 15. Calculate the running total revenue for each product category.
SELECT
    p.category,
    SUM(s.total_price) AS sales_revenue
FROM
    products p
    JOIN sales s ON p.product_id = s.product_id
GROUP BY
    p.category;

-- 16. Categorize sales as "High", "Medium", or "Low" based on total price.
SELECT
    sale_id,
    product_id,
    total_price,
    CASE
        WHEN total_price >= 1000 THEN 'High'
        WHEN total_price >= 500 THEN 'Medium'
        ELSE 'Low'
    END AS sale_category
FROM
    Sales;

-- 17. Identify sales where the quantity sold is greater than the average quantity sold.
SELECT
    *
FROM
    sales
WHERE
    quantity_sold > (
        SELECT
            AVG(quantity_sold)
        FROM
            sales
    );

-- 18. Extract the month and year from the sale date and count the number of sales for each month.
SELECT
    YEAR (sale_date) AS sale_year,
    MONTH (sale_date) AS sale_month,
    COUNT(*) AS sales_count
FROM
    Sales
GROUP BY
    YEAR (sale_date),
    MONTH (sale_date)
ORDER BY
    sale_year,
    sale_month;

-- 19. Calculate the number of days between the current date and the sale date for each sale.
SELECT
    sale_id,
    sale_date,
    DATEDIFF (CURDATE (), sale_date) AS days_since_sale
FROM
    Sales;

-- 20. Identify sales made during weekdays versus weekends.
SELECT
    sale_id,
    sale_date,
    CASE
        WHEN WEEKDAY (sale_date) < 5 THEN "Weekdays"
        ELSE "weekends"
    END as day_type
FROM
    sales;