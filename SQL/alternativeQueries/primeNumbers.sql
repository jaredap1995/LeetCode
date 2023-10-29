with 
recursive AllNumbers (n) as (
    select 1
    union all
    select n+1
    from allNumbers 
    where n<100
) select group_concat (Num.n seperator "&") from AllNumbers Num
where not exists ( --Using the where not exists to elminiate all values that are not prime
    select n from allNumbers Factors
    where factors.n > 1 and factors.n<Num.n and Num.n%Factors.n=0
) and Num.n >1;