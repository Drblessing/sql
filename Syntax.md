## String Matching

```
SELECT * FROM PATIENTS WHERE
CONDITIONS LIKE '% DIAB1%' OR
CONDITIONS LIKE 'DIAB1%';
```

## Group String Concat

```
SELECT sell_date, COUNT(DISTINCT product) AS num_sold, GROUP_CONCAT(DISTINCT product ORDER BY product) AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date
```

## String Editing

Using Left, Right

```
SELECT user_id, CONCAT(UPPER(left(name,1)),LOWER(right(name,length(name)-1))) as name
FROM Users
ORDER BY user_id
```

Using SUBSTR

```
SELECT user_id,CONCAT(UPPER(SUBSTR(name,1,1)),LOWER(SUBSTR(name,2,length(name)))) AS name
FROM Users ORDER BY user_id;
```

## Case

```
SELECT e.employee_id,
CASE WHEN e.employee_id%2=1 AND e.name NOT LIKE 'M%' THEN salary ELSE 0 END AS bonus
FROM Employees e ORDER BY e.employee_id
```

## Subquery Not exists

```
SELECT C.name as Customers
FROM Customers c
WHERE NOT EXISTS (SELECT 1 FROM Orders o WHERE o.customerId = c.id)
```

## Inner Join remove duplicates conditional

```
DELETE p1
FROM Person p1, Person p2
WHERE p1.email = p2.email AND p1.id > p2.id
```

## Window function dense rank

```
SELECT d.name Department,t.name Employee,t.salary Salary
FROM (SELECT departmentId, name, salary,
dense_rank() OVER (PARTITION BY departmentid ORDER BY salary DESC) r
FROM Employee) t
LEFT JOIN Department d ON d.id = t.departmentId
WHERE r <= 3
```

## Functions

```
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M = N-1;
  RETURN (
      SELECT DISTINCT salary
      FROM Employee e
      ORDER BY salary DESC
      LIMIT M,1
  );
END
```

## IFNULL

```
SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary
```

## Update

```
UPDATE Salary SET sex =
(CASE WHEN sex = 'm' THEN 'f' ELSE 'm' END);
```
