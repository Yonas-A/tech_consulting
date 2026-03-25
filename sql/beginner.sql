-- 1. Retrieve all columns from the Sales table.
SELECT 
    *
FROM
    sales;

-- 2. Retrieve the product_name and unit_price from the Products table.
SELECT 
    product_name, unit_price
FROM
    products;

-- 3. Retrieve the sale_id and sale_date from the Sales table.
SELECT 
    sale_id, sale_date
FROM
    sales;

-- 4. Filter the Sales table to show only sales with a total_price greater than $100.
SELECT 
    *
FROM
    sales
WHERE
    total_price > 100;

-- 5. Filter the Products table to show only products in the 'Electronics' category.
SELECT 
    *
FROM
    products
WHERE
    category = 'Electronics';

-- 6. Retrieve the sale_id and total_price from the Sales table for sales made on January 3, 2024.
SELECT 
    sale_id, total_price
FROM
    sales
WHERE
    sale_date = '2024-01-03';

-- 7. Retrieve the product_id and product_name from the Products table for products with a unit_price greater than $100.
SELECT 
    product_id, product_name
FROM
    products
WHERE
    unit_price > 100;

-- 8. Calculate the total revenue generated from all sales in the Sales table.
SELECT 
    SUM(total_price)
FROM
    sales;

-- 9. Calculate the average unit_price of products in the Products table.
SELECT 
    AVG(unit_price)
FROM
    products;

-- 10. Calculate the total quantity_sold from the Sales table.
SELECT 
    SUM(quantity_sold)
FROM
    sales;

-- 11. Count Sales Per Day from the Sales table.
SELECT 
    SUM(quantity_sold), sale_date AS sales_per_day
FROM
    sales
GROUP BY sale_date;

-- 12. Retrieve product_name and unit_price from the Products table with the Highest Unit Price.
SELECT 
    product_name, unit_price
FROM
    products
WHERE
    unit_price = (SELECT 
            MAX(unit_price)
        FROM
            products);

-- 13. Retrieve the sale_id, product_id, and total_price from the Sales table for sales with a quantity_sold greater than 4.
SELECT 
    sale_id, product_id, total_price
FROM
    sales
WHERE
    quantity_sold > 4;

-- 14. Retrieve the product_name and unit_price from the Products table, ordering the results by  unit_price in descending order.
SELECT 
    product_name, unit_price
FROM
    products
ORDER BY unit_price DESC;

-- 15. Retrieve the total_price of all sales, rounding the values to two decimal places.
SELECT 
    sale_id, ROUND(total_price, 2) AS rounded_price
FROM
    sales;


-- 16. Calculate the average total_price of sales in the Sales table.
SELECT 
    AVG(total_price)
FROM
    sales;

-- 17. Retrieve the sale_id and sale_date from the Sales table, formatting the sale_date as 'YYYY-MM-DD'.
SELECT 
    sale_id, DATE_FORMAT(sale_date, '%y-%m-%d') AS FormattedDate
FROM
    sales;

-- 18. Calculate the total revenue generated from sales of products in the 'Electronics' category.
SELECT 
    SUM(total_price)
FROM
    sales s
        JOIN
    products p ON p.product_id = s.product_id
WHERE
    p.category = 'Electronics';



-- 19. Retrieve the product_name and unit_price from the Products table, filtering the unit_price to show only values between $20 and $600.
SELECT 
    product_name, unit_price
FROM
    products
WHERE
    unit_price BETWEEN 20 AND 600;

-- 20. Retrieve the product_name and category from the Products table, ordering the results by category in ascending order.
SELECT 
    product_name, category
FROM
    products
ORDER BY category;
