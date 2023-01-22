Solution 1: Subquery with group by 

```
SELECT COUNT(company_id) as co_w_duplicate_jobs
FROM (SELECT j1.company_id
FROM job_listings j1
GROUP BY title,description,company_id
HAVING COUNT(job_id) > 1) j1
```

