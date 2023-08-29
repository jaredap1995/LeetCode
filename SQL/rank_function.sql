--example 

with cte as (
    SELECT id, email,
    Rank() OVER (PARTITION BY Name, Email, ORDER BY ID) AS RankNo
    FROM customer
) DELETE FROM CTE where RankNo > 1;

--For client session duplicate removal

WITH cte as (
    select id, session_date, client_id,
    Rank() OVER (Partition by session_date, client_id ORDER BY ID) as UniqueSessions
    from sessions
) DELETE from cte where UniqueSessions > 1;

--^^^above does not work in postgres. Must delete directlhy from table as opposed to cte
WITH cte as (
    select id,
    Rank() OVER (partition by session_date, client_id order by id) as UniqueSessions
    from sessions
) delete from sessions where id in (
    SELECT id from cte where UniqueSessions >1
); -- This works but I have foreign key constraint.