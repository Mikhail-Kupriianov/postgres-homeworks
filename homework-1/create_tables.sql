-- SQL-команды для создания таблиц
CREATE TABLE employees
(
    employer_id int2 PRIMARY KEY,
    first_name varchar(50) NOT NULL,
	last_name varchar(50) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date date NOT NULL,
    notes text NOT NULL
);

CREATE TABLE customers
(
    customer_id char(5) PRIMARY KEY,
    company_name varchar(100) NOT NULL,
	contact_name varchar(100) NOT NULL
);

CREATE TABLE orders
(
    order_id int2 PRIMARY KEY,
    customer_id char(5) REFERENCES customers(customer_id) NOT NULL,
	employee_id int2 REFERENCES employees(employer_id) NOT NULL,
	order_date date NOT NULL,
	ship_city varchar(50) NOT NULL
);