drop database if exists tutorial;
create database tutorial;
use tutorial;

-- Create Products table
CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    unit_price DECIMAL(10 , 2 )
);

INSERT INTO Products (product_id, product_name, category, unit_price)
VALUES
(101, 'Laptop', 'Electronics', 500.00),
(102, 'Smartphone', 'Electronics', 300.00),
(103, 'Headphones', 'Electronics', 30.00),
(104, 'Keyboard', 'Electronics', 20.00),
(105, 'Mouse', 'Electronics', 15.00),
-- additional rows for visuals
(106, 'Lemons', 'Fruit', 5.00),
(107, 'Banana', 'Fruit', 7.00),
(108, 'Tea', 'Drink', 3.50);


CREATE TABLE Sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    quantity_sold INT,
    sale_date DATE,
    total_price DECIMAL(10 , 2 ),
    FOREIGN KEY (product_id)
        REFERENCES Products (product_id)
);
        
    -- Insert sample data into Sales table
INSERT INTO Sales (sale_id, product_id, quantity_sold, sale_date,
total_price) VALUES
(1, 101, 5, '2024-01-01', 2500.00),
(2, 102, 3, '2024-01-02', 900.00),
(3, 103, 2, '2024-01-02', 60.00),
(4, 104, 4, '2024-01-03', 80.00),
(5, 105, 6, '2024-01-03', 90.00),
-- additional values for better visualization of intermediate and advanced questions
(6, 106, 100, '2024-01-04', 500.00),
(7, 107, 50, '2024-01-04', 350.00),
(8, 107, 26, '2024-02-01', 188.00),
(9, 101, 10, '2024-03-27', 5000.00);

