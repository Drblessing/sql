```
SELECT page_id
FROM pages
WHERE NOT EXISTS (SELECT NULL FROM page_likes WHERE page_likes.page_id = pages.page_id)
ORDER BY page_id;
```

Solution 2: Left Outer Join
```
SELECT pages.page_id
FROM pages
LEFT OUTER JOIN page_likes AS likes
  ON pages.page_id = likes.page_id
WHERE likes.page_id IS NULL;
```

Solution 3: Using EXCEPT

```
SELECT page_id
FROM pages
EXCEPT
SELECT page_id
FROM page_likes
ORDER BY page_id;
```