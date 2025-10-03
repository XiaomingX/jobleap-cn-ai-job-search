# 100 SQL Fundamental Interview Questions and Answers


### 1. What is SQL?
**Answer:**  
SQL (Structured Query Language) is a standard programming language used for managing and manipulating relational databases. It allows users to perform tasks such as querying data, updating records, deleting data, and creating and modifying database structures.
```sql
SELECT * FROM employees;
```

---

### 2. What is a primary key?
**Answer:**  
A primary key is a unique identifier for a record in a database table. It ensures that each record can be uniquely identified and helps to establish relationships between tables. A primary key cannot contain NULL values.
```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100)
);
```

---

### 3. What is a foreign key?
**Answer:**  
A foreign key is a column or a set of columns in one table that uniquely identifies a row of another table. It creates a relationship between the two tables and enforces referential integrity.
```sql
CREATE TABLE departments (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);
```

---

### 4. What is a JOIN in SQL?
**Answer:**  
A JOIN clause is used to combine rows from two or more tables based on a related column between them. Common types of JOINs include:
- **INNER JOIN**
- **LEFT JOIN**
- **RIGHT JOIN**
- **FULL OUTER JOIN**
```sql
-- INNER JOIN
SELECT employees.name, departments.name
FROM employees
INNER JOIN departments ON employees.department_id = departments.id;

-- LEFT JOIN
SELECT employees.name, departments.name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.id;

-- RIGHT JOIN
SELECT employees.name, departments.name
FROM employees
RIGHT JOIN departments ON employees.department_id = departments.id;

-- FULL OUTER JOIN
SELECT employees.name, departments.name
FROM employees
FULL OUTER JOIN departments ON employees.department_id = departments.id;
```

---

### 5. What is the difference between INNER JOIN and OUTER JOIN?
**Answer:**  
- **INNER JOIN:** Returns only the rows where there is a match in both tables involved in the join. If there are no matching rows, the result is null.
- **OUTER JOIN:** Includes all rows from one table and the matching rows from the other table. If there is no match, it returns null for the columns from the table without a match. This can be further divided into:
  - **LEFT JOIN:** Includes all rows from the left table.
  - **RIGHT JOIN:** Includes all rows from the right table.
```sql
-- INNER JOIN
SELECT employees.name, departments.name
FROM employees
INNER JOIN departments ON employees.department_id = departments.id;

-- LEFT JOIN
SELECT employees.name, departments.name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.id;

-- RIGHT JOIN
SELECT employees.name, departments.name
FROM employees
RIGHT JOIN departments ON employees.department_id = departments.id;

-- FULL OUTER JOIN
SELECT employees.name, departments.name
FROM employees
FULL OUTER JOIN departments ON employees.department_id = departments.id;
```

---

### 6. What is a subquery?
**Answer:**  
A subquery is a query nested inside another query. It is used to perform intermediate steps in complex queries, often for filtering results or performing calculations that are then used by the main query.
```sql
-- Subquery to find employees with salary greater than the average salary
SELECT name
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

---

### 7. How do you handle NULL values in SQL?
**Answer:**  
- **Using `COALESCE`:** Replace NULL values with a specified value.
- **Filtering out NULLs:** Use a condition in the WHERE clause to exclude rows with NULL values, e.g., `WHERE column IS NOT NULL`.
```sql
-- Using COALESCE to replace NULL values
SELECT COALESCE(salary, 0) FROM employees;

-- Filtering out NULLs
SELECT * FROM employees WHERE salary IS NOT NULL;
```

---

### 8. What is the difference between DELETE and TRUNCATE?
**Answer:**  
- **DELETE:** Removes specified rows from a table based on a condition and can be rolled back if used within a transaction. It also fires any associated triggers.
- **TRUNCATE:** Removes all rows from a table without logging individual row deletions and cannot be rolled back in most databases. TRUNCATE is faster than DELETE and resets any identity columns.
```sql
-- DELETE
DELETE FROM employees WHERE department_id = 1;

-- TRUNCATE
TRUNCATE TABLE employees;
```

---

### 9. What is a stored procedure?
**Answer:**  
A stored procedure is a precompiled collection of one or more SQL statements stored in the database. It is used to encapsulate repetitive tasks, improve performance by reducing the need to compile SQL code multiple times, and enhance security by controlling access to data.
```sql
-- Example of a stored procedure
CREATE PROCEDURE GetEmployeeDetails
AS
BEGIN
    SELECT * FROM employees;
END;
```

---

### 10. What is indexing in SQL?
**Answer:**  
Indexing is a technique used to improve the performance of SQL queries by reducing the amount of data that needs to be scanned. An index is created on a table column, and it helps the database to find rows more quickly and efficiently.
```sql
CREATE INDEX idx_employee_name ON employees(name);
```

---

### 11. What is normalization in SQL?
**Answer:**  
Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity. It involves dividing large tables into smaller ones and defining relationships between them. Common normalization forms include:
- **1NF (First Normal Form)**
- **2NF (Second Normal Form)**
- **3NF (Third Normal Form)**
- **BCNF (Boyce-Codd Normal Form)**
```sql
-- Example of normalization (1NF to 3NF)
-- 1NF: Single table with redundant data
CREATE TABLE employees (
    id INT,
    name VARCHAR(100),
    department VARCHAR(100),
    department_location VARCHAR(100)
);

-- 2NF: Removing partial dependencies
CREATE TABLE departments (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100)
);

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

-- 3NF: Removing transitive dependencies
CREATE TABLE departments (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE locations (
    department_id INT PRIMARY KEY,
    location VARCHAR(100)
);

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);
```
---

### 12. What is denormalization?
**Answer:**  
Denormalization is the process of combining normalized tables to improve read performance. It involves adding redundant data to one or more tables to avoid complex joins and improve query execution time.
```sql
-- Example of denormalization: combining two tables into one
CREATE TABLE employee_details (
    id INT,
    name VARCHAR(100),
    department VARCHAR(100),
    department_location VARCHAR(100)
);
```
---

### 13. What is a view in SQL?
**Answer:**  
A view is a virtual table based on the result-set of an SQL query. It contains rows and columns just like a real table and can be used to simplify complex queries, enhance security by restricting access to specific data, and present data in a specific format.
```sql
-- Example of creating a view
CREATE VIEW employee_departments AS
SELECT employees.name, departments.name AS department_name
FROM employees
INNER JOIN departments ON employees.department_id = departments.id;
```
---

### 14. How do you create a view in SQL?
**Answer:**  
To create a view, use the `CREATE VIEW` statement followed by the view name and the `AS` keyword with the SELECT query. Example:
```sql
CREATE VIEW employee_departments AS
SELECT employees.name, departments.name AS department_name
FROM employees
INNER JOIN departments ON employees.department_id = departments.id;
```
---

### 15. What is a trigger in SQL?
**Answer:**  
A trigger is a stored procedure that automatically executes in response to certain events on a particular table or view. Triggers can be used for enforcing business rules, validating input data, and maintaining audit trails.
```sql
-- Example of a trigger
CREATE TRIGGER trgAfterInsert ON employees
FOR INSERT
AS
BEGIN
    PRINT 'New employee record inserted';
END;
```
---

### 16. What is a transaction in SQL?
**Answer:**  
A transaction is a sequence of one or more SQL operations treated as a single unit of work. Transactions ensure data integrity by following the ACID properties (Atomicity, Consistency, Isolation, Durability). A transaction can be started with the `BEGIN TRANSACTION` statement and completed with `COMMIT` or `ROLLBACK`.
```sql
-- Example of a transaction
BEGIN TRANSACTION;
INSERT INTO employees (id, name, department) VALUES (2, 'Jane Doe', 'Finance');
COMMIT;
```
---

### 17. What is the difference between COMMIT and ROLLBACK?
**Answer:**  
- **COMMIT:** Saves all changes made in the transaction to the database permanently.
- **ROLLBACK:** Reverts all changes made in the transaction, restoring the database to its previous state before the transaction began.
```sql
-- Example of COMMIT
BEGIN TRANSACTION;
INSERT INTO employees (id, name, department) VALUES (3, 'Mike Smith', 'IT');
COMMIT;

-- Example of ROLLBACK
BEGIN TRANSACTION;
INSERT INTO employees (id, name, department) VALUES (4, 'Anna Johnson', 'HR');
ROLLBACK;
```
---

### 18. What are aggregate functions in SQL?
**Answer:**  
Aggregate functions perform calculations on multiple rows of a table and return a single value. Common aggregate functions include:
- **SUM()**: Calculates the total sum of a numeric column.
- **AVG()**: Calculates the average value of a numeric column.
- **COUNT()**: Counts the number of rows.
- **MIN()**: Finds the minimum value in a column.
- **MAX()**: Finds the maximum value in a column.
```sql
-- Example of aggregate functions
SELECT COUNT(*), AVG(salary), MAX(salary), MIN(salary), SUM(salary)
FROM employees;
```
---

### 19. What is the GROUP BY clause in SQL?
**Answer:**  
The `GROUP BY` clause groups rows that have the same values in specified columns into summary rows. It is often used with aggregate functions to perform calculations on each group. Example:
```sql
-- Example of GROUP BY
SELECT department, COUNT(*), AVG(salary)
FROM employees
GROUP BY department;
```
---

### 20. What is the HAVING clause in SQL?
**Answer:**  
The `HAVING` clause is used to filter groups of rows created by the `GROUP BY` clause based on a specified condition. Unlike the `WHERE` clause, which filters individual rows, `HAVING` filters groups. Example:
```sql
-- Example of HAVING
SELECT department, COUNT(*), AVG(salary)
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;
```

---

### 21. What is the difference between WHERE and HAVING clause?
**Answer:**  
- **WHERE Clause:** Filters individual rows before any groupings are made. It cannot be used with aggregate functions.
- **HAVING Clause:** Filters groups of rows after the `GROUP BY` clause. It can be used with aggregate functions.
```sql
-- Example of WHERE
SELECT * FROM employees WHERE salary > 50000;

-- Example of HAVING
SELECT department, AVG(salary)
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;
```
---

### 22. What is a UNION operator in SQL?
**Answer:**  
The `UNION` operator is used to combine the result sets of two or more SELECT queries. Each SELECT statement within the UNION must have the same number of columns in the result sets with similar data types. It removes duplicate rows between the various SELECT statements.
```sql
-- Example of UNION
SELECT name FROM employees
UNION
SELECT name FROM managers;
```
---

### 23. What is the difference between UNION and UNION ALL?
**Answer:**  
- **UNION:** Combines the result sets of two or more SELECT queries and removes duplicate rows.
- **UNION ALL:** Combines the result sets of two or more SELECT queries and includes duplicate rows.
```sql
-- Example of UNION
SELECT name FROM employees
UNION
SELECT name FROM managers;

-- Example of UNION ALL
SELECT name FROM employees
UNION ALL
SELECT name FROM managers;
```
---

### 24. What is the purpose of the DISTINCT keyword in SQL?
**Answer:**  
The `DISTINCT` keyword is used to remove duplicate rows from the result set of a SELECT query. It ensures that the returned results contain only unique values.
```sql
-- Example of DISTINCT
SELECT DISTINCT department FROM employees;
```
---

### 25. What are the different types of SQL commands?
**Answer:**  
SQL commands are divided into several categories:
- **DDL (Data Definition Language):** Includes commands like CREATE, ALTER, DROP.
- **DML (Data Manipulation Language):** Includes commands like SELECT, INSERT, UPDATE, DELETE.
- **DCL (Data Control Language):** Includes commands like GRANT, REVOKE.
- **TCL (Transaction Control Language):** Includes commands like COMMIT, ROLLBACK, SAVEPOINT.
- **DQL (Data Query Language):** Primarily includes the SELECT command.
```sql
-- Example of DDL command
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100)
);

-- Example of DML command
INSERT INTO employees (id, name, department)
VALUES (1, 'John Doe', 'HR');

-- Example of DCL command
GRANT SELECT ON employees TO user_name;

-- Example of TCL command
COMMIT;
```
---

### 26. What is a constraint in SQL?
**Answer:**  
A constraint is a rule applied to a column or a table to enforce data integrity and consistency. Common types of constraints include:
- **NOT NULL**
- **UNIQUE**
- **PRIMARY KEY**
- **FOREIGN KEY**
- **CHECK**
- **DEFAULT**
```sql
-- Example of constraints
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    department_id INT,
    salary DECIMAL CHECK (salary > 0),
    FOREIGN KEY (department_id) REFERENCES departments(id)
);
```
---

### 27. What is a schema in SQL?
**Answer:**  
A schema is a logical container for database objects such as tables, views, indexes, and procedures. It helps organize and manage database objects and can also provide a level of security by allowing different users to access specific schemas.
```sql
-- Example of creating a schema
CREATE SCHEMA sales;
CREATE TABLE sales.employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100)
);
```
---

### 28. What is the difference between CHAR and VARCHAR data types?
**Answer:**  
- **CHAR:** A fixed-length character data type. It always uses the specified number of bytes, regardless of the length of the stored string.
- **VARCHAR:** A variable-length character data type. It uses only as many bytes as necessary to store the string, up to the specified maximum length.
```sql
-- Example of CHAR and VARCHAR
CREATE TABLE products (
    product_code CHAR(10),
    product_name VARCHAR(100)
);
```
---

### 29. What is a composite key?
**Answer:**  
A composite key is a combination of two or more columns in a table that together serve as a unique identifier for a record. Each column in the composite key can contain duplicate values, but the combination of all columns must be unique.
```sql
-- Example of a composite key
CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    PRIMARY KEY (order_id, product_id)
);
```
---

### 30. What is referential integrity?
**Answer:**  
Referential integrity is a property that ensures that relationships between tables remain consistent. When one table has a foreign key that points to another table, referential integrity ensures that the foreign key value matches a primary key value in the referenced table, or is NULL.
```sql
-- Example of referential integrity
CREATE TABLE departments (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);
```
---

### 31. What is an alias in SQL?
**Answer:**  
An alias is a temporary name given to a table or column for the duration of a SQL query. It is used to make column names more readable and to simplify complex queries.
```sql
-- Example of an alias
SELECT e.name AS employee_name, d.name AS department_name
FROM employees e
JOIN departments d ON e.department_id = d.id;
```
---

### 32. What is a default constraint in SQL?
**Answer:**  
A default constraint is used to set a default value for a column when no value is specified during an insert operation. It ensures that the column always contains a value.
```sql
-- Example of a default constraint
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100) DEFAULT 'General'
);
```
---

### 33. What is the difference between a clustered and a non-clustered index?
**Answer:**  
- **Clustered Index:** Sorts and stores the data rows in the table based on the index key. There can be only one clustered index per table.
- **Non-Clustered Index:** Creates a separate structure from the data rows. The index contains pointers to the data rows. There can be multiple non-clustered indexes per table.
```sql
-- Example of clustered and non-clustered index
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100)
);

-- Clustered index on the primary key
CREATE CLUSTERED INDEX idx_id ON employees(id);

-- Non-clustered index on the name column
CREATE NONCLUSTERED INDEX idx_name ON employees(name);
```
---

### 34. What is a candidate key in SQL?
**Answer:**  
A candidate key is a column, or a set of columns, that can uniquely identify a row in a table. A table can have multiple candidate keys, but one of them will be chosen as the primary key.
```sql
-- Example of candidate keys
CREATE TABLE employees (
    id INT,
    ssn VARCHAR(11),
    email VARCHAR(100),
    PRIMARY KEY (id),
    UNIQUE (ssn),
    UNIQUE (email)
);
```
---

### 35. What is a self-join?
**Answer:**  
A self-join is a join in which a table is joined with itself. It is useful for querying hierarchical data or comparing rows within the same table.
```sql
-- Example of a self-join
SELECT e1.name AS employee_name, e2.name AS manager_name
FROM employees e1
JOIN employees e2 ON e1.manager_id = e2.id;
```
---

### 36. What is a sequence in SQL?
**Answer:**  
A sequence is a database object that generates a sequence of unique numeric values according to a specified increment. Sequences are commonly used to generate unique primary key values.
```sql
-- Example of a sequence
CREATE SEQUENCE emp_sequence
START WITH 1
INCREMENT BY 1;

-- Using the sequence to insert data
INSERT INTO employees (id, name, department)
VALUES (NEXT VALUE FOR emp_sequence, 'John Doe', 'HR');
```
---

### 37. What is the purpose of the LIKE operator in SQL?
**Answer:**  
The `LIKE` operator is used in a `WHERE` clause to search for a specified pattern in a column. It is often used with wildcards:
- `%` represents zero, one, or multiple characters.
- `_` represents a single character.
```sql
-- Example of LIKE operator
SELECT * FROM employees
WHERE name LIKE 'J%';
```
---

### 38. What is a synonym in SQL?
**Answer:**  
A synonym is an alias or alternative name for a database object such as a table, view, sequence, or stored procedure. Synonyms make it easier to reference objects and can help with database schema management.
```sql
-- Example of creating a synonym
CREATE SYNONYM emp FOR employees;
SELECT * FROM emp;
```
---

### 39. What is data integrity?
**Answer:**  
Data integrity refers to the accuracy, consistency, and reliability of data stored in a database. It is maintained through the use of constraints, triggers, and transactions to ensure that the data remains valid and consistent.
```sql
-- Example of data integrity using constraints
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);
```
---

### 40. What is the ACID property in SQL?
**Answer:**  
The ACID properties ensure reliable processing of database transactions:
- **Atomicity:** Ensures that all operations within a transaction are completed successfully; otherwise, the transaction is aborted.
- **Consistency:** Ensures that a transaction brings the database from one valid state to another.
- **Isolation:** Ensures that the operations of one transaction are isolated from those of other transactions.
- **Durability:** Ensures that the results of a committed transaction are permanently saved in the database.
```sql
-- Example of a transaction demonstrating ACID properties
BEGIN TRANSACTION;
INSERT INTO employees (id, name, department) VALUES (5, 'Robert Brown', 'Sales');
COMMIT;
```

---

### 41. What is the purpose of the ORDER BY clause in SQL?
**Answer:**  
The `ORDER BY` clause is used to sort the result set of a query by one or more columns. By default, it sorts in ascending order; however, it can also sort in descending order using the `DESC` keyword.
```sql
-- Example of ORDER BY
SELECT * FROM employees ORDER BY salary DESC;
```
---

### 42. What is a unique key in SQL?
**Answer:**  
A unique key is a constraint that ensures all values in a column or a set of columns are unique across the table. Unlike the primary key, a table can have multiple unique keys, and unique keys can contain NULL values.
```sql
-- Example of a unique key
CREATE TABLE employees (
    id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE
);
```
---

### 43. What is the purpose of the CASE statement in SQL?
**Answer:**  
The `CASE` statement is used to create conditional logic in SQL queries. It allows you to return different values based on specified conditions, similar to an if-else statement in programming languages.
```sql
-- Example of CASE statement
SELECT name,
    CASE
        WHEN salary > 50000 THEN 'High'
        WHEN salary BETWEEN 30000 AND 50000 THEN 'Medium'
        ELSE 'Low'
    END AS salary_level
FROM employees;
```
---

### 44. What is the purpose of the LIMIT clause in SQL?
**Answer:**  
The `LIMIT` clause is used to restrict the number of rows returned by a query. It is often used in conjunction with the `ORDER BY` clause to return a subset of the result set.
```sql
-- Example of LIMIT
SELECT * FROM employees ORDER BY salary DESC LIMIT 10;
```
---

### 45. What is a cross join in SQL?
**Answer:**  
A cross join, also known as a Cartesian join, returns the Cartesian product of the two tables involved in the join. This means it returns all possible combinations of rows from the two tables.
```sql
-- Example of CROSS JOIN
SELECT employees.name, departments.name AS department_name
FROM employees
CROSS JOIN departments;
```
---

### 46. What is the difference between an alias and a synonym in SQL?
**Answer:**  
- **Alias:** A temporary name given to a table or column in a SQL query for the duration of that query.
- **Synonym:** A permanent alias for a database object, which remains until explicitly dropped.
```sql
-- Example of alias
SELECT e.name AS employee_name, d.name AS department_name
FROM employees e
JOIN departments d ON e.department_id = d.id;

-- Example of synonym
CREATE SYNONYM emp FOR employees;
SELECT * FROM emp;
```
---

### 47. What is the difference between SQL and PL/SQL?
**Answer:**  
- **SQL:** A standard language for managing and manipulating relational databases.
- **PL/SQL:** A procedural language extension for SQL, used in Oracle databases to write complex scripts and functions.
```sql
-- Example of PL/SQL procedure
CREATE OR REPLACE PROCEDURE GetEmployeeDetails
IS
BEGIN
    SELECT * FROM employees;
END;
/
```
---

### 48. What is a foreign key constraint in SQL?
**Answer:**  
A foreign key constraint is a rule that maintains referential integrity between two tables. It ensures that the value in a foreign key column matches a value in the primary key column of the referenced table.
```sql
-- Example of foreign key constraint
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);
```
---

### 49. What is the purpose of the NVL function in SQL?
**Answer:**  
The `NVL` function is used to replace NULL values with a specified value. It is commonly used to ensure that calculations and operations are performed correctly even when some data is missing.
```sql
-- Example of NVL function
SELECT name, NVL(salary, 0) AS salary
FROM employees;
```
---

### 50. What is a subquery in SQL?
**Answer:**  
A subquery is a query nested inside another query. It is used to perform intermediate steps in complex queries, often for filtering results or performing calculations that are then used by the main query.
```sql
-- Example of subquery
SELECT name
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```
---

### 51. What is a correlated subquery in SQL?
**Answer:**  
A correlated subquery is a subquery that references columns from the outer query. It is executed once for each row processed by the outer query and is used to perform row-by-row processing.
```sql
-- Example of correlated subquery
SELECT e1.name, e1.salary
FROM employees e1
WHERE e1.salary > (SELECT AVG(e2.salary) FROM employees e2 WHERE e2.department_id = e1.department_id);
```
---

### 52. What is the purpose of the COALESCE function in SQL?
**Answer:**  
The `COALESCE` function returns the first non-NULL value in a list of expressions. It is used to handle NULL values by providing a default value when NULLs are encountered.
```sql
-- Example of COALESCE function
SELECT name, COALESCE(salary, 0) AS salary
FROM employees;
```
---

### 53. What is a bitmap index in SQL?
**Answer:**  
A bitmap index is a type of index that uses bitmaps (binary arrays) to represent the existence of values in a table. Bitmap indexes are efficient for columns with a low cardinality (few distinct values) and are used to improve query performance.
```sql
-- Example of bitmap index (Oracle syntax)
CREATE BITMAP INDEX idx_employee_department ON employees(department_id);
```
---

### 54. What is the purpose of the ROW_NUMBER() function in SQL?
**Answer:**  
The `ROW_NUMBER()` function assigns a unique sequential integer to rows within a result set. It is often used for pagination or to provide a unique identifier for rows in a query result.
```sql
-- Example of ROW_NUMBER() function
SELECT name, salary,
       ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num
FROM employees;
```
---

### 55. What is the difference between RANK() and DENSE_RANK() in SQL?
**Answer:**  
- **RANK():** Assigns a rank to each row within a partition, with gaps in the ranking sequence for ties.
- **DENSE_RANK():** Assigns a rank to each row within a partition without gaps in the ranking sequence for ties.
```sql
-- Example of RANK() and DENSE_RANK() functions
SELECT name, salary,
       RANK() OVER (ORDER BY salary DESC) AS rank,
       DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank
FROM employees;
```
---

### 56. What is the purpose of the CAST() function in SQL?
**Answer:**  
The `CAST()` function is used to convert an expression from one data type to another. It is commonly used to ensure that data types are compatible in expressions and comparisons.
```sql
-- Example of CAST() function
SELECT name, CAST(salary AS VARCHAR(10)) AS salary_str
FROM employees;
```
---

### 57. What is a materialized view in SQL?
**Answer:**  
A materialized view is a database object that stores the result of a query physically. It is used to improve query performance by precomputing and storing complex query results, reducing the need to recompute them each time.
```sql
-- Example of materialized view (Oracle syntax)
CREATE MATERIALIZED VIEW emp_dept_view AS
SELECT e.name, d.name AS department_name
FROM employees e
JOIN departments d ON e.department_id = d.id;
```
---

### 58. What is the difference between INNER JOIN and CROSS JOIN?
**Answer:**  
- **INNER JOIN:** Returns only the rows where there is a match in both tables based on the specified condition.
- **CROSS JOIN:** Returns the Cartesian product of two tables, including all possible combinations of rows from both tables.
```sql
-- Example of INNER JOIN
SELECT e.name, d.name AS department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id;

-- Example of CROSS JOIN
SELECT e.name, d.name AS department_name
FROM employees e
CROSS JOIN departments d;
```
---

### 59. What is a recursive query in SQL?
**Answer:**  
A recursive query is a query that refers to itself, typically using a common table expression (CTE). It is used to perform hierarchical or tree-structured data retrieval.
```sql
-- Example of recursive query using CTE
WITH RECURSIVE EmployeeHierarchy AS (
    SELECT id, name, manager_id
    FROM employees
    WHERE manager_id IS NULL
    UNION ALL
    SELECT e.id, e.name, e.manager_id
    FROM employees e
    INNER JOIN EmployeeHierarchy eh ON e.manager_id = eh.id
)
SELECT * FROM EmployeeHierarchy;
```
---

### 60. What is the purpose of the GROUP_CONCAT() function in SQL?
**Answer:**  
The `GROUP_CONCAT()` function concatenates values from multiple rows into a single string, separated by a specified delimiter. It is used to aggregate and display multiple values from a group as a single string.
```sql
-- Example of GROUP_CONCAT() function
SELECT department, GROUP_CONCAT(name SEPARATOR ', ') AS employees
FROM employees
GROUP BY department;
```
---

### 61. What is the purpose of the IFNULL function in SQL?
**Answer:**  
The `IFNULL` function returns a specified value if the given expression is NULL. If the expression is not NULL, it returns the expression itself. It is used to handle NULL values by providing a default value.
```sql
-- Example of IFNULL function
SELECT name, IFNULL(salary, 0) AS salary
FROM employees;
```
---

### 62. What is the difference between a primary key and a unique key?
**Answer:**  
- **Primary Key:** Uniquely identifies each row in a table and does not allow NULL values. A table can have only one primary key.
- **Unique Key:** Ensures that all values in a column or a set of columns are unique. It allows NULL values (only one per column) and a table can have multiple unique keys.
```sql
-- Example of primary key
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

-- Example of unique key
CREATE TABLE employees (
    id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE
);
```
---

### 63. What is a lateral view in SQL?
**Answer:**  
A lateral view is used in conjunction with a table-generating function to enable the output of the function to be joined with the original table. It is often used in data transformation and analysis tasks.
```sql
-- Example of lateral view (Hive syntax)
SELECT e.name, t.skill
FROM employees e
LATERAL VIEW explode(skills) t AS skill;
```
---

### 64. What is the purpose of the CURRENT_DATE function in SQL?
**Answer:**  
The `CURRENT_DATE` function returns the current date of the system. It is used to retrieve the current date for use in queries and calculations.
```sql
-- Example of CURRENT_DATE function
SELECT CURRENT_DATE AS today;
```
---

### 65. What is a composite index in SQL?
**Answer:**  
A composite index is an index on two or more columns of a table. It is used to improve the performance of queries that filter or sort data based on multiple columns.
```sql
-- Example of composite index
CREATE INDEX idx_name_department ON employees(name, department);
```
---

### 66. What is the purpose of the AUTO_INCREMENT attribute in SQL?
**Answer:**  
The `AUTO_INCREMENT` attribute is used to generate a unique identifier for new rows in a table automatically. It is often applied to primary key columns to ensure that each row has a unique identifier.
```sql
-- Example of AUTO_INCREMENT
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100)
);
```
---

### 67. What is a table alias in SQL?
**Answer:**  
A table alias is a temporary name given to a table within a query. It is used to make the query more readable and to simplify references to the table, especially in complex queries involving joins.
```sql
-- Example of table alias
SELECT e.name, d.name AS department_name
FROM employees e
JOIN departments d ON e.department_id = d.id;
```
---

### 68. What is the difference between COUNT(*) and COUNT(column_name)?
**Answer:**  
- **COUNT(*):** Counts all rows in the table, including rows with NULL values.
- **COUNT(column_name):** Counts non-NULL values in the specified column.
```sql
-- Example of COUNT(*)
SELECT COUNT(*) FROM employees;

-- Example of COUNT(column_name)
SELECT COUNT(department) FROM employees;
```
---

### 69. What is the purpose of the TO_DATE function in SQL?
**Answer:**  
The `TO_DATE` function converts a string to a date data type. It is used to transform string representations of dates into actual date values for use in queries and calculations.
```sql
-- Example of TO_DATE function
SELECT TO_DATE('2024-01-01', 'YYYY-MM-DD') AS date_value;
```
---

### 70. What is the purpose of the CASE WHEN statement in SQL?
**Answer:**  
The `CASE WHEN` statement is used to implement conditional logic in SQL queries. It allows different values to be returned based on specified conditions, similar to an if-else statement in programming languages.
```sql
-- Example of CASE WHEN statement
SELECT name,
    CASE
        WHEN salary > 50000 THEN 'High'
        WHEN salary BETWEEN 30000 AND 50000 THEN 'Medium'
        ELSE 'Low'
    END AS salary_level
FROM employees;
```
---

### 71. What is the purpose of the GETDATE() function in SQL?
**Answer:**  
The `GETDATE()` function returns the current date and time of the system. It is used to retrieve the current timestamp for use in queries and calculations.
```sql
-- Example of GETDATE() function
SELECT GETDATE() AS current_timestamp;
```
---

### 72. What is a partitioned table in SQL?
**Answer:**  
A partitioned table is a large table that is divided into smaller, more manageable pieces called partitions. Each partition can be accessed and maintained separately, which can improve query performance and manageability.
```sql
-- Example of partitioned table (Oracle syntax)
CREATE TABLE sales (
    sale_id INT,
    sale_date DATE,
    amount DECIMAL
)
PARTITION BY RANGE (sale_date) (
    PARTITION p1 VALUES LESS THAN (TO_DATE('2023-01-01', 'YYYY-MM-DD')),
    PARTITION p2 VALUES LESS THAN (TO_DATE('2024-01-01', 'YYYY-MM-DD'))
);
```
---

### 73. What is the difference between TRUNCATE and DROP?
**Answer:**  
- **TRUNCATE:** Removes all rows from a table but retains the table structure for future use. It is faster than DELETE and cannot be rolled back in most databases.
- **DROP:** Deletes the table and its structure from the database entirely.
```sql
-- Example of TRUNCATE
TRUNCATE TABLE employees;

-- Example of DROP
DROP TABLE employees;
```
---

### 74. What is a cursor in SQL?
**Answer:**  
A cursor is a database object used to retrieve, manipulate, and navigate through a result set row by row. Cursors are useful for processing individual rows returned by a query.
```sql
-- Example of cursor (PL/SQL syntax)
DECLARE
    CURSOR emp_cursor IS
    SELECT name, salary FROM employees;
    emp_record emp_cursor%ROWTYPE;
BEGIN
    OPEN emp_cursor;
    LOOP
        FETCH emp_cursor INTO emp_record;
        EXIT WHEN emp_cursor%NOTFOUND;
        DBMS_OUTPUT.PUT_LINE(emp_record.name || ' - ' || emp_record.salary);
    END LOOP;
    CLOSE emp_cursor;
END;
/
```
---

### 75. What is an inline view in SQL?
**Answer:**  
An inline view is a subquery in the FROM clause of a SQL statement. It acts as a temporary table for the duration of the query and can simplify complex queries by breaking them down into smaller, more manageable parts.
```sql
-- Example of inline view
SELECT name, department_name
FROM (SELECT e.name, d.name AS department_name
      FROM employees e
      JOIN departments d ON e.department_id = d.id);
```
---

### 76. What is the difference between IS NULL and IS NOT NULL?
**Answer:**  
- **IS NULL:** Checks whether a column value is NULL.
- **IS NOT NULL:** Checks whether a column value is not NULL.
```sql
-- Example of IS NULL
SELECT * FROM employees WHERE salary IS NULL;

-- Example of IS NOT NULL
SELECT * FROM employees WHERE salary IS NOT NULL;
```
---

### 77. What is the purpose of the CONCAT function in SQL?
**Answer:**  
The `CONCAT` function is used to concatenate two or more strings into a single string. It is commonly used to combine values from different columns or to add static text to query results.
```sql
-- Example of CONCAT function
SELECT CONCAT(name, ' - ', department) AS employee_info
FROM employees;
```
---

### 78. What is a data warehouse in SQL?
**Answer:**  
A data warehouse is a centralized repository that stores large volumes of data from multiple sources. It is used for reporting, analysis, and decision-making processes. Data in a data warehouse is typically structured and optimized for read-heavy queries.
```sql
-- Example of creating a data warehouse table
CREATE TABLE fact_sales (
    sale_id INT,
    product_id INT,
    customer_id INT,
    sale_date DATE,
    amount DECIMAL
);
```
---

### 79. What is a surrogate key in SQL?
**Answer:**  
A surrogate key is a unique identifier for a record in a table that is not derived from application data. It is typically an auto-incremented number and is used as a primary key.
```sql
-- Example of surrogate key
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100)
);
```
---

### 80. What is the purpose of the LEFT function in SQL?
**Answer:**  
The `LEFT` function is used to extract a specified number of characters from the left side of a string. It is commonly used to manipulate and format string data.
```sql
-- Example of LEFT function
SELECT LEFT(name, 3) AS name_prefix
FROM employees;
```

---

### 81. What is the purpose of the RIGHT function in SQL?
**Answer:**  
The `RIGHT` function is used to extract a specified number of characters from the right side of a string. It is commonly used to manipulate and format string data.
```sql
-- Example of RIGHT function
SELECT RIGHT(name, 3) AS name_suffix
FROM employees;
```
---

### 82. What is a star schema in SQL?
**Answer:**  
A star schema is a type of database schema that is commonly used in data warehousing and business intelligence. It consists of a central fact table surrounded by dimension tables. The fact table contains quantitative data, while dimension tables contain descriptive attributes.
```sql
-- Example of star schema
CREATE TABLE fact_sales (
    sale_id INT,
    sale_date DATE,
    product_id INT,
    customer_id INT,
    amount DECIMAL
);

CREATE TABLE dim_product (
    product_id INT,
    product_name VARCHAR(100),
    category VARCHAR(50)
);

CREATE TABLE dim_customer (
    customer_id INT,
    customer_name VARCHAR(100),
    location VARCHAR(100)
);
```
---

### 83. What is a snowflake schema in SQL?
**Answer:**  
A snowflake schema is a type of database schema that is a more normalized form of the star schema. In a snowflake schema, dimension tables are normalized into multiple related tables, reducing redundancy and improving data integrity.
```sql
-- Example of snowflake schema
CREATE TABLE fact_sales (
    sale_id INT,
    sale_date DATE,
    product_id INT,
    customer_id INT,
    amount DECIMAL
);

CREATE TABLE dim_product (
    product_id INT,
    product_name VARCHAR(100),
    category_id INT
);

CREATE TABLE dim_category (
    category_id INT,
    category_name VARCHAR(50)
);

CREATE TABLE dim_customer (
    customer_id INT,
    customer_name VARCHAR(100),
    location_id INT
);

CREATE TABLE dim_location (
    location_id INT,
    location_name VARCHAR(100)
);
```
---

### 84. What is the difference between the EQUI JOIN and NON-EQUI JOIN?
**Answer:**  
- **EQUI JOIN:** A type of join that uses the equality operator (`=`) to match rows between tables based on a common column.
- **NON-EQUI JOIN:** A type of join that uses operators other than the equality operator (such as `<`, `>`, `<=`, `>=`, `<>`) to match rows between tables.
```sql
-- Example of EQUI JOIN
SELECT e.name, d.name AS department_name
FROM employees e
JOIN departments d ON e.department_id = d.id;

-- Example of NON-EQUI JOIN
SELECT e.name, s.grade
FROM employees e
JOIN salary_grades s ON e.salary BETWEEN s.min_salary AND s.max_salary;
```
---

### 85. What is the purpose of the LENGTH function in SQL?
**Answer:**  
The `LENGTH` function returns the number of characters in a string. It is used to determine the length of string data.
```sql
-- Example of LENGTH function
SELECT name, LENGTH(name) AS name_length
FROM employees;
```
---

### 86. What is a fact table in SQL?
**Answer:**  
A fact table is a central table in a star or snowflake schema in a data warehouse. It contains quantitative data (facts) and foreign keys to dimension tables. Fact tables are used to store metrics and measures for analysis and reporting.
```sql
-- Example of a fact table
CREATE TABLE fact_sales (
    sale_id INT,
    sale_date DATE,
    product_id INT,
    customer_id INT,
    amount DECIMAL
);
```
---

### 87. What is a dimension table in SQL?
**Answer:**  
A dimension table is a table in a star or snowflake schema in a data warehouse. It contains descriptive attributes (dimensions) related to the facts in the fact table. Dimension tables are used to provide context and meaning to the facts for analysis and reporting.
```sql
-- Example of a dimension table
CREATE TABLE dim_product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50)
);
```
---

### 88. What is the purpose of the REPLACE function in SQL?
**Answer:**  
The `REPLACE` function is used to replace occurrences of a specified substring within a string with another substring. It is commonly used to modify and clean string data.
```sql
-- Example of REPLACE function
SELECT REPLACE(name, 'John', 'Jonathan') AS updated_name
FROM employees;
```
---

### 89. What is the difference between the DATE and TIMESTAMP data types in SQL?
**Answer:**  
- **DATE:** Stores date values (year, month, day) without time.
- **TIMESTAMP:** Stores date and time values (year, month, day, hour, minute, second, fractional seconds).
```sql
-- Creating a table with DATE and TIMESTAMP columns
CREATE TABLE events (
    event_id INT PRIMARY KEY,
    event_date DATE,
    event_timestamp TIMESTAMP
);

-- Inserting data into the table
INSERT INTO events (event_id, event_date, event_timestamp) 
VALUES (1, '2024-01-01', '2024-01-01 10:00:00');

-- Selecting data from the table
SELECT * FROM events;
```
---

### 90. What is a common table expression (CTE) in SQL?
**Answer:**  
A common table expression (CTE) is a temporary result set that can be referenced within a SELECT, INSERT, UPDATE, or DELETE statement. It is defined using the `WITH` keyword and provides a way to simplify complex queries and improve readability.
```sql
-- Example of a common table expression (CTE)
WITH EmployeeCTE AS (
    SELECT name, department_id, salary
    FROM employees
    WHERE salary > 50000
)
SELECT * FROM EmployeeCTE;
```
---

### 91. What is the purpose of the SUBSTRING function in SQL?
**Answer:**  
The `SUBSTRING` function is used to extract a part of a string based on specified starting position and length. It is commonly used to manipulate and format string data.
```sql
-- Example of SUBSTRING function
SELECT SUBSTRING(name, 1, 3) AS name_prefix
FROM employees;
```
---

### 92. What is a bitmap join index in SQL?
**Answer:**  
A bitmap join index is a type of index that combines the advantages of bitmap indexes and join indexes. It is used to improve the performance of join queries by precomputing the join result and storing it as a bitmap index.
```sql
-- Example of bitmap join index (Oracle syntax)
CREATE BITMAP JOIN INDEX idx_emp_dept ON employees(department_id)
FROM employees JOIN departments ON employees.department_id = departments.id;
```
---

### 93. What is a sequence in SQL?
**Answer:**  
A sequence is a database object that generates a sequence of unique numeric values according to a specified increment. Sequences are commonly used to generate unique primary key values.
```sql
-- Example of sequence (Oracle syntax)
CREATE SEQUENCE emp_sequence
START WITH 1
INCREMENT BY 1;

-- Using the sequence to insert data
INSERT INTO employees (id, name, department)
VALUES (emp_sequence.NEXTVAL, 'John Doe', 'HR');
```
---

### 94. What is a lateral join in SQL?
**Answer:**  
A lateral join is a join that allows a subquery in the FROM clause to reference columns from preceding tables in the same FROM clause. It is used to create more complex queries with correlated subqueries.
```sql
-- Example of lateral join (PostgreSQL syntax)
SELECT e.name, t.skill
FROM employees e
JOIN LATERAL (
    SELECT skill
    FROM skills s
    WHERE s.employee_id = e.id
) t;
```
---

### 95. What is the purpose of the NULLIF function in SQL?
**Answer:**  
The `NULLIF` function returns NULL if the two specified expressions are equal; otherwise, it returns the first expression. It is used to handle special cases where certain values need to be treated as NULL.
```sql
-- Example of NULLIF function
SELECT name, NULLIF(salary, 0) AS salary
FROM employees;
```
---

### 96. What is a histogram in SQL?
**Answer:**  
A histogram is a statistical representation of the distribution of values in a column. It is used by the query optimizer to improve query performance by providing information about the data distribution.
```sql
-- Example of creating a histogram (Oracle syntax)
BEGIN
    DBMS_STATS.GATHER_TABLE_STATS('HR', 'EMPLOYEES', METHOD_OPT => 'FOR ALL COLUMNS SIZE AUTO');
END;
/
```
---

### 97. What is the purpose of the DATEPART function in SQL?
**Answer:**  
The `DATEPART` function extracts a specific part of a date (such as year, month, day, hour) from a date or timestamp value. It is used to perform date-based calculations and formatting.
```sql
-- Example of DATEPART function (SQL Server syntax)
SELECT name, DATEPART(year, hire_date) AS hire_year
FROM employees;
```
---

### 98. What is a materialized view log in SQL?
**Answer:**  
A materialized view log is a table associated with a materialized view that records changes to the base table. It is used to refresh the materialized view incrementally by capturing only the changes since the last refresh.
```sql
-- Example of creating a materialized view log (Oracle syntax)
CREATE MATERIALIZED VIEW LOG ON employees
WITH PRIMARY KEY, ROWID;
```
---

### 99. What is the difference between the ROLLUP and CUBE operators in SQL?
**Answer:**  
- **ROLLUP:** Generates subtotals that roll up from the most detailed level to a grand total.
- **CUBE:** Generates subtotals for all possible combinations of a group of columns, including a grand total.
```sql
-- Example of ROLLUP
SELECT department, job_title, SUM(salary)
FROM employees
GROUP BY ROLLUP(department, job_title);

-- Example of CUBE
SELECT department, job_title, SUM(salary)
FROM employees
GROUP BY CUBE(department, job_title);
```
---

### 100. What is the purpose of the TRANSLATE function in SQL?
**Answer:**  
The `TRANSLATE` function replaces each occurrence of a character in a string with another specified character. It is commonly used to perform character replacements and data cleaning.
```sql
-- Example of TRANSLATE function
SELECT TRANSLATE(name, 'aeiou', '12345') AS translated_name
FROM employees;
```
---



If you found this repository helpful, please give it a star!

Follow me on:
- [LinkedIn](https://www.linkedin.com/in/ashish-jangra/)
- [GitHub](https://github.com/AshishJangra27)
- [Kaggle](https://www.kaggle.com/ashishjangra27)


Stay updated with my latest content and projects!
