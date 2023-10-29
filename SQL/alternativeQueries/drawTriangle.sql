--MS Server Approach: Iterative, not neccesarily best way for dealing with SQl as it is better to deal with sets of data

DECLARE @n INT = 1

while @n <= 20
Begin
    Print REPLICATE("* ", n)
    SET @n = @n +1
END;


with recursive nums(n) as (
    select 1
    union all
    select n+1
    from nums
    where n<20
)

select repeat("* ",n) as pattern from nums;