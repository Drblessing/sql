Solution: Extract date, group

```
SELECT sender_id,COUNT(message_id) as message_count
FROM messages m1
WHERE EXTRACT(MONTH FROM sent_date) = 08 AND
EXTRACT(YEAR FROM sent_date) = 2022
GROUP BY sender_id
ORDER BY COUNT(*) DESC
LIMIT 2
```
