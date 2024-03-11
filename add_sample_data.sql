-- add_sample_data.sql

-- Inserting sample data into the tables
INSERT INTO departments (department_id, department_name)
VALUES
    (1, 'IT'),
    (2, 'HR'),
    (3, 'Finance');

INSERT INTO employees (employee_id, first_name, last_name, department_id)
VALUES
    (1, 'Faith', 'Chepkoech', 1),
    (2, 'Jane', 'Williams', 2),
    (3, 'Mike', 'Aliceson', 1),
    (4, 'Emily', 'Brown', 3);
