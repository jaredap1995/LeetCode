-- order results descending if distinct
-- if more than one achieved same score sort result by ascending hacker_id
-- total score = sum of max score for all of their challenges
-- exclude all hackers with score of 0

SELECT 
    cte.hacker_id,
    cte.name,
    SUM(maxscores) as scores
FROM
        (SELECT 
            h.hacker_id,   
            h.name,
            max(s.score) as maxscores,
            s.challenge_id
        FROM hackers h
        JOIN submissions s on h.hacker_id = s.hacker_id
        GROUP BY h.hacker_id, h.name, s.challenge_id) 
    as cte
GROUP BY cte.hacker_id, cte.name
HAVING scores > 0
ORDER BY score desc, cte.hacker_id asc;

