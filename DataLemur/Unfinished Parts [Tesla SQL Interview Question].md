SELECT DISTINCT(part)
FROM parts_assembly
WHERE parts_assembly.finish_date is NULL;
