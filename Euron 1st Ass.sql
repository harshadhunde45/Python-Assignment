
/*1 Design a database schema for an online bookstore, including tables for books,
 authors, customers, and orders. Define appropriate data types, primary keys, 
 foreign keys, and constraints for each table. Provide the SQL CREATE TABLE statements for each table */
 
/* Online Bookstore – Database Schema (Complete)
📌 Tables:
customers
authors
books
orders
order_items (important for many-to-many relation) */
  
create database  if not exists online_bookstore ;
use online_bookstore ;
CREATE TABLE customers (
    cust_id INT AUTO_INCREMENT PRIMARY KEY,
    cust_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(50) NOT NULL,
    bio TEXT
);

CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    price DECIMAL(8,2) CHECK (price > 0),
    stock INT DEFAULT 0 CHECK (stock >= 0),
    author_id INT,
    published_date DATE,
    
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    cust_id INT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'Pending',
    
    FOREIGN KEY (cust_id) REFERENCES customers(cust_id)
);

CREATE TABLE order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    book_id INT,
    quantity INT CHECK (quantity > 0),
    price DECIMAL(8,2) NOT NULL,
    
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);

/* 2 Write a series of SQL statements to perform the following actions on a table named 'products' (assume the table 
already exists with columns 'id', 'name', 'price', and 'category'):
Add a new column named 'description' of type VARCHAR(255).
Modify the 'price' column to be of type DECIMAL(10, 2).
Remove the 'category' column.
Rename the table to 'inventory'. */



 
 




****************************************************************************************************************************
/*Assignment 1:: Complete the following questions for self-evaluation

1 Design a database schema for an online bookstore, including tables for books,
 authors, customers, and orders. Define appropriate data types, primary keys, 
 foreign keys, and constraints for each table. Provide the SQL CREATE TABLE statements for each table

2 Write a series of SQL statements to perform the following actions on a table named 'products' 
(assume the table already exists with columns 'id', 'name', 'price', and 'category'):

Add a new column named 'description' of type VARCHAR(255).
Modify the 'price' column to be of type DECIMAL(10, 2).
Remove the 'category' column.
Rename the table to 'inventory'.

3 Explain the difference between a primary key and a foreign key. Illustrate your explanation with a 
concrete example using the 'students', 'courses', and 'enrollments' tables discussed in the lecture.
 Describe how these keys enforce referential integrity.

4 Implement a function (in any programming language) that takes two table names (e.g., 'students' and 'courses') 
and a relationship type ('one-to-many' or 'many-to-many') as input. The function should generate 
the appropriate SQL CREATE TABLE statement for a linking table that establishes the specified
 relationship between the two tables. Assume both tables have an 'id' column as their primary key.

5 Given the following SQL schema:

CREATE TABLE employees ( employee_id INT PRIMARY KEY AUTO_INCREMENT, first_name VARCHAR(50) NOT NULL, last_name 
VARCHAR(50) NOT NULL, department_id INT, salary DECIMAL(10, 2) );
CREATE TABLE departments ( department_id INT PRIMARY KEY AUTO_INCREMENT, department_name VARCHAR(100) NOT NULL );
Write SQL INSERT INTO statements to populate both tables with at least 5 rows of sample data each. Then, write a 
SELECT statement that retrieves the first name, last name, and department name for all employees.

6 Consider a scenario where you need to store historical data for product prices. Design a database schema that 
includes a 'products' table and a 'product_prices' table. The 'product_prices' table should store the product ID, 
price, and the date the price was effective from. Explain how you would handle price changes over time using this 
schema, and provide example SQL queries to retrieve the current price of a product and the price history for a 
specific product.