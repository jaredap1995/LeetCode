WITH hacker_stats as (select 
    h.hacker_id, 
    h.name,
    count(c.challenge_id) as num
FROM hackers h
    inner join challenges c on h.hacker_id = c.hacker_id
GROUP BY 
    h.hacker_id, h.name
ORDER BY 
    num desc, h.hacker_id asc
),
-- create a challenge stats table with columns
-- Num, count of num


-- Create a maxchallenge table (will be equal to a single value select statement)


--Create join query with subqueries that returns the result
