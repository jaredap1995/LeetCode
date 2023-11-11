with cte as (
    select distinct s.submission_date 
    -- Distinct s.submission_date is the combination of the two subqueries below
    (
        select count(distinct s1.hacker_id) from 
        submissions s1 where s1.submission_date = s.submission_date
        and (
            select count(distinct s2.submission_date)
            from submissions s2 where s2.hacker_id = s1.hacker_id
            and s2.submission_date < s.submission_date
        ) = datediff(day, '2016-03-01', s1.submission_date)
    ) as counthacker,

    -- h_id is a result of the subquery below
    (
        select top 1 s1.hacker_id
        from submissions s1
        where s1.submission_date = s.submission_date
        order by count(s1.submission_id) desc, s1.hacker_id asc 
    )
    as h_id from submissions s
)
select cte.submission_date, cte.counthacker, cte.h_id, h.name
join hackers h on h.hacker_id = cte.h_id
order by cte.submission_date;