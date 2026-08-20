DROP TABLE IF EXISTS company_customer;
CREATE TABLE IF NOT EXISTS company_customer (
    customer_id   INTEGER PRIMARY KEY,
    name          TEXT    NOT NULL,
    product_line  TEXT    NOT NULL,
    export_country TEXT   NOT NULL,
    order_value    REAL    NOT NULL
);

INSERT INTO company_customer VALUES (1, 'Albert Ross',     'Electronics', 'Canada',        12500.00);
INSERT INTO company_customer VALUES (2, 'Amanda Torres',   'Furniture',   'Mexico',         8400.00);
INSERT INTO company_customer VALUES (3, 'Aaron Morgan',    'Electronics', 'United Kingdom',21000.00);
INSERT INTO company_customer VALUES (4, 'Arthur Pendelton','Clothing',    'Australia',      4300.00);
INSERT INTO company_customer VALUES (5, 'Carlos Orton',    'Furniture',   'Canada',         9200.00);
INSERT INTO company_customer VALUES (6, 'Anna Jordan',     'Clothing',    'Germany',        6100.00);
INSERT INTO company_customer VALUES (7, 'Robert Taylor',   'Electronics', 'Mexico',        15500.00);
INSERT INTO company_customer VALUES (8, 'Alice Gregory',   'Leisure',     'United Kingdom', 3200.00);

SELECT DISTINCT product_line FROM company_customer;
SELECT DISTINCT export_country FROM company_customer;
SELECT * FROM company_customer WHERE name LIKE 'A%';
SELECT * FROM company_customer WHERE name LIKE '%or%';
SELECT * FROM company_customer WHERE product_line = 'Electronics';
SELECT * FROM company_customer WHERE order_value >= 10000.00;
SELECT * FROM company_customer WHERE export_country IN ('Canada', 'Mexico', 'United Kingdom');

SELECT product_line, COUNT(*) AS customer_count, SUM(order_value) AS total_sales
FROM company_customer
GROUP BY product_line;

SELECT export_country, AVG(order_value) AS avg_order_value
FROM company_customer
GROUP BY export_country
HAVING AVG(order_value) >= 8000.00;

SELECT * FROM company_customer ORDER BY order_value DESC LIMIT 4;
