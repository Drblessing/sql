```sql
SELECT row_number() over (order by counts) as ranks, count(*) as users_num
from (SELECT count(*) as counts FROM tweets
GROUP BY user_id) counts
group by counts
order by ranks
```
