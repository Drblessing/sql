```
SELECT page_id
FROM pages
WHERE NOT EXISTS (SELECT NULL FROM page_likes WHERE page_likes.page_id = pages.page_id)
ORDER BY page_id;
```
