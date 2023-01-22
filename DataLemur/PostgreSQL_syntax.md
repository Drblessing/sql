# PostgreSQL 14

## Basics

Strings are denoted with single-quotes. 'string here'.

For string methods, like `where`, you can use a tuple:

```
WHERE skill IN ('Python', 'Java')
```

## Functions

```
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
```

## Keywords

### Exists / Not Exists

Corerlated subquery, condition in the middle subquery

```
SELECT  l.*
FROM    t_left l
WHERE   NOT EXISTS
        (
        SELECT  NULL
        FROM    t_right r
        WHERE   r.value = l.value
        )
```

### SUM

Aggregate function that will sum numerical value

### Count

Will count rows, even blank ones

### CASE

Syntax:

```
CASE WHEN [Condition] THEN [true value] ELSE [false value] END
```

Example:

```
CASE WHEN device_type in ('tablet','phone') THEN 1 ELSE 0 END
```
