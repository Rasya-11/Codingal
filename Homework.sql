-- Create the Employees table for DXC Company
CREATE TABLE IF NOT EXISTS Employees (
    emp_id TEXT PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary REAL,
    status TEXT
);

-- Insert sample records, including those under investigation
INSERT INTO Employees (emp_id, name, department, salary, status) VALUES
('E101', 'Tarun', 'Management', 85000.0, 'Active'),
('E102', 'John Doe', 'Finance', 62000.0, 'Suspicious'),
('E103', 'Jane Smith', 'Sales', 58000.0, 'Active'),
('E104', 'Alex Lyon', 'Finance', 71000.0, 'Suspicious');

-- Fetch all employee records to view the dataset
SELECT * FROM Employees;

-- Fetch details of specific employees involved in the fraud investigation
SELECT name, department, status 
FROM Employees 
WHERE status = 'Suspicious';
