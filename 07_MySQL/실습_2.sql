-- USE classicmodels;

-- SELECT customerName FROM customers;


-- SELECT * FROM orders ORDER BY orderDate DESC LIMIT 10;


-- SELECT * FROM payments WHERE amount >= 100;

-- 조인 쿼리 --
-- SELECT o.orderNumber, c.customerName
-- FROM orders o
-- JOIN customers c ON o.customerNumber = c.customerNumber;


-- SELECT p.productName, p.productLine, pl.textDescription
-- FROM products p
-- JOIN productlines pl ON p.productLine = pl.productLine;


-- SELECT e1.employeeNumber, e1.firstName, e1.lastName, e2.firstName AS 'ManagerFirstName', e2.lastName AS 'ManagerLastName'
-- FROM employees e1
-- LEFT JOIN employees e2 ON e1.reportsTo = e2.employeeNumber;

-- SELECT e.employeeNumber, e.lastName, e.firstName, e.extension, e.email, e.officeCode, e.reportsTo, e.jobTitle
-- FROM employees e
-- JOIN offices o ON e.officeCode = o.officeCode
-- WHERE o.city = 'San Francisco';

-- 그룹쿼리 --
-- 제품 라인별 제품 수: 각 제품 라인에 속한 제품의 수를 조회하세요.
-- SELECT productLine, COUNT(*) AS productCount
-- FROM products
-- GROUP BY productLine;


-- 고객별 총 주문 금액: 각 고객별로 총 주문 금액을 계산하세요.
-- SELECT customers.customerNumber, 
--        customers.customerName, 
--        SUM(orderdetails.quantityOrdered * orderdetails.priceEach) AS totalAmount
-- FROM customers
-- JOIN orders ON customers.customerNumber = orders.customerNumber
-- JOIN orderdetails ON orders.orderNumber = orderdetails.orderNumber
-- GROUP BY customers.customerNumber, customers.customerName;

-- USE classicmodels
-- SELECT orderNumber, SUM(quantityOrdered * priceEach) AS totalAmount
-- FROM orderdetails
-- GROUP BY orderNumber
-- HAVING totalAmount > 500;


-- INSERT INTO customers (customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit)
-- VALUES ('New Customer', 'Lastname', 'Firstname', '123-456-7890', '123 Street', 'Suite 1', 'City', 'State', 'PostalCode', 'Country', 1002, 50000.00);

-- UPDATE products
-- SET buyPrice = buyPrice * 1.10
-- WHERE productLine = 'Classic Cars';

-- UPDATE customers
-- SET email = 'newemail@example.com'
-- WHERE customerNumber = 103;

-- UPDATE employees
-- SET officeCode = '2'
-- WHERE employeeNumber = 1002;