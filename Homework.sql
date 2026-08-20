DROP TABLE IF EXISTS employee;
CREATE TABLE IF NOT EXISTS employee (
    employee_id   INTEGER PRIMARY KEY,
    name          TEXT    NOT NULL,
    department    TEXT    NOT NULL,
    salary        REAL    NOT NULL,
    hire_date     TEXT    NOT NULL,
    performance_rating REAL
);

INSERT INTO employee VALUES (1, 'Alice Smith',   'Engineering', 85000.00,  '2021-03-15', 4.5);
INSERT INTO employee VALUES (2, 'Bob Jones',     'Marketing',   62000.00,  '2022-06-01', 3.8);
INSERT INTO employee VALUES (3, 'Charlie Brown', 'Engineering', 95000.00,  '2020-01-10', 4.8);
INSERT INTO employee VALUES (4, 'Diana Prince', 'Finance',     78000.00,  '2023-02-28', 4.2);
INSERT INTO employee VALUES (5, 'Evan Wright',   'Marketing',   58000.00,  '2024-01-15', 3.5);
INSERT INTO employee VALUES (6, 'Fiona Gallagher','HR',         55000.00,  '2021-11-01', 4.0);
INSERT INTO employee VALUES (7, 'George Clark',  'Finance',     82000.00,  '2019-07-22', 4.7);
INSERT INTO employee VALUES (8, 'Hannah Abbott', 'HR',         52000.00,  '2023-08-14', 3.9);

SELECT * FROM employee;
UPDATE employee SET salary = 65000.00 WHERE employee_id = 2;
SELECT name, salary FROM employee ORDER BY salary DESC;
SELECT name, department, hire_date FROM employee ORDER BY department ASC, hire_date DESC;
SELECT name, salary FROM employee ORDER BY salary DESC LIMIT 3;
SELECT name, department, salary FROM employee WHERE department = 'Engineering';
SELECT name, salary FROM employee WHERE salary >= 70000.00 AND performance_rating >= 4.0;
SELECT department, COUNT(*) AS employee_count FROM employee GROUP BY department;

SELECT department, SUM(salary) AS total_payroll, AVG(salary) AS avg_salary
FROM employee
GROUP BY department;

SELECT department, AVG(salary) AS avg_salary
FROM employee
GROUP BY department
HAVING AVG(salary) >= 65000.00;
