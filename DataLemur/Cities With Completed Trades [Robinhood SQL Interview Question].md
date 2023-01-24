Solution: Join

```
SELECT users.city,COUNT(trades.order_id)
FROM trades
JOIN users
ON users.user_id = trades.user_id
WHERE status = 'Completed'
GROUP BY users.city
ORDER BY COUNT(trades.order_id) DESC
LIMIT 3
```
