CREATE database SALES1
USE SALES1
CREATE TABLE sales_data_final (
	order_id VARCHAR(15) NOT NULL, 
	order_date DATE NOT NULL, 
	ship_date DATE NOT NULL, 
	ship_mode VARCHAR(14) NOT NULL, 
	customer_name VARCHAR(22) NOT NULL, 
	segment VARCHAR(11) NOT NULL, 
	state VARCHAR(36) NOT NULL, 
	country VARCHAR(32) NOT NULL, 
	market VARCHAR(6) NOT NULL, 
	region VARCHAR(14) NOT NULL, 
	product_id VARCHAR(16) NOT NULL, 
	category VARCHAR(15) NOT NULL, 
	sub_category VARCHAR(11) NOT NULL, 
	product_name VARCHAR(127) NOT NULL, 
	sales DECIMAL(38, 0) NOT NULL, 
	quantity DECIMAL(38, 0) NOT NULL, 
	discount DECIMAL(38, 3) NOT NULL, 
	profit DECIMAL(38, 5) NOT NULL, 
	shipping_cost DECIMAL(38, 2) NOT NULL, 
	order_priority VARCHAR(8) NOT NULL, 
	`year` DECIMAL(38, 0) NOT NULL
);

select * from sales_data_final;

SET SESSION sql_mode = ''
SET GLOBAL local_infile=1; 




load data local infile 
'C:/Users/shiva/Downloads/a.csv'
into table sales_data_final
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 rows ;

select * from  sales_data_final;









load data local infile 
‪'D:\salesdata.csv'
into table sales_data_final
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 rows

