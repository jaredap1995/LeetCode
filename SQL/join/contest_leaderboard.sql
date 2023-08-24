-- total score = sum of max score for all of their challenges
-- order results descending if distinct
-- if more than one achieved same score sort result by ascending hacker_id
-- exclude all hackers with score of 0
SELECT 
    cte.hacker_id,
    cte.name,
    sum(maxscore) AS sumofmax
FROM 
    (
        SELECT  
            h.hacker_id,
            h.name,
            s.challenge_id,
            max(score) AS maxscore
        FROM
            hackers h
            INNER JOIN submissions s
        WHERE 
            h.hacker_id = s.hacker_id
        GROUP BY 
            h.hacker_id,
            h.name,
            s.challenge_id
    ) as cte
GROUP BY 
    cte.hacker_id,
    ctre.name
HAVING 
    sumofmax > 0
ORDER BY 
    sumofmax desc, cte.hacker_id asc