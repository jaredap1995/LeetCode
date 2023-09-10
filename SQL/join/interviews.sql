--Need cte that joins 
WITH user_challenges AS (
    SELECT 
        c.contest_id,
        c.hacker_id,
        c.name,
        co.college_id,
        ch.challenge_id
    FROM contests c
    JOIN colleges co ON co.contest_id = c.contest_id
    JOIN challenges ch ON ch.college_id = co.college_id
), 
view_subCTE AS (
    SELECT
        s.challenge_id,  
        s.total_submissions,
        s.total_accepted_submissions,
        v.total_views,
        v.total_unique_views
    FROM submission_stats s
    JOIN view_stats v ON v.challenge_id = s.challenge_id
    GROUP BY s.challenge_id
)
SELECT 
    u.contest_id,
    u.hacker_id,
    u.name, 
    SUM(vs.total_submissions) AS total_submissions, 
    SUM(vs.total_accepted_submissions) AS total_accepted_submissions, 
    SUM(vs.total_views) AS total_views, 
    SUM(vs.total_unique_views) AS total_unique_views
FROM user_challenges u
LEFT JOIN view_subCTE vs ON vs.challenge_id = u.challenge_id
WHERE (
    vs.total_submissions >0 AND 
    vs.total_accepted_submissions > 0 AND 
    vs.total_views > 0 AND 
    vs.total_unique_views > 0
)
GROUP BY u.contest_id, u.hacker_id, u.name
ORDER BY u.contest_id;



--
select
    f1.contest_id,
    f1.hacker_id,
    f1.name,
    sum(sum_total_subs) as sum1,
    sum(sum_total_acc_subs) as sum2,
    sum(sum_total_view) as sum3,
    sum(sum_total_unique_view) as sum4
from
    (
        select
            cts.contest_id,
            cts.hacker_id,
            cts.name,
            colg.college_id,
            chall.challenge_id
        from
            contests as cts
            join colleges as colg on cts.contest_id = colg.contest_id
            join challenges as chall on chall.college_id = colg.college_id
    ) as f1
    left join (
        select
            challenge_id,
            sum(total_views) as sum_total_view,
            sum(total_unique_views) as sum_total_unique_view
        from
            view_stats
        group by
            challenge_id
    ) as f2 on f1.challenge_id = f2.challenge_id
    left join (
        select
            challenge_id,
            sum(total_submissions) as sum_total_subs,
            sum(total_accepted_submissions) as sum_total_acc_subs
        from
            submission_stats
        group by
            challenge_id
    ) as f3 on f1.challenge_id = f3.challenge_id
group by
    f1.contest_id,
    f1.hacker_id,
    f1.name
having
    (
        sum(sum_total_view) + sum(sum_total_unique_view) + sum(sum_total_subs) + sum(sum_total_acc_subs)
    ) > 0
order by
    f1.contest_id;