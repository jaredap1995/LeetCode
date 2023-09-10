-- SOlution 1
--row number is used to make sure we do not compare a row to itself
--We need a cross-join to return every row from the first and every row from the second table (comparing to itself)
--We make sure to include the t1.row_num != t2.row_num because we do not want to compare a row with itself


WITH table1 as (
    SELECT *, Row_number() OVER (order by x,y) as row_num from functions
)
SELECT t1.x, t2.y from table1 t1 CROSS JOIN table1 t2
WHERE t1.row_num != t2.row_num AND t1.x = t2.y AND t1.y = t2.x AND t1.x <= t1.y
GROUP BY t1.x, t1.y
order by t1.x;

--Solution 2

SELECT * from functions where x=y GROUP BY x,y HAVING count(x) >1
Union
SELECT * from (select f1.x, f1.y from functions f1 cross join functions f2 
where f1.x = f2.y and f1.y = f2.x and f1.x != f1.y AND f2.y != f1.y
GROUP BY f1.x, f1.y) as new_tb
where x<=y
order by x