-- create_tables.sql

-- Creating a simple database schema
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department_id INT
);

CREATE TABLE department (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);
