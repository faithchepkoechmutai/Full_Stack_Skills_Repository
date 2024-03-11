-- basic_queries.sql

-- Basic SELECT queries
SELECT * FROM employees;

SELECT first_name, last_name FROM employees WHERE department_id = 1;

SELECT department_name, COUNT(employee_id) AS employee_count
FROM employees
JOIN departments ON employees.department_id = departments.department_id
GROUP BY department_name;
