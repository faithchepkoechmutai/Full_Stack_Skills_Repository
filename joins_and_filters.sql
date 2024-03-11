-- joins_and_filters.sql

-- Joining tables and applying filters
SELECT first_name, last_name, department_name
FROM employees
JOIN departments ON employees.department_id = departments.department_id
WHERE department_name = 'IT';
