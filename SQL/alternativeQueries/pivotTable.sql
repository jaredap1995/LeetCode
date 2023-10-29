--MS Server with Pivot Function
select doctor, professor, singer, actor from(
    select name, occupation, 
    row_number() over(partition by occupation order by occupation asc, name asc) as num
    from occupations
) as src pivot (
    max(name)
    for occupation in (doctor, professor, singer, actor)
) as pvt

--MySQL
SELECT 
    max(case when occupation = 'doctor' then name else null end) as doctor,
    max(case when occupation = 'professor' then name else null end) as professor,
    max(case when occupation = 'singer' then name else null end) as singer,
    max(case when occupation 'actor' then name else end) as actor
from
    (
        select
        name, occupation,
        row_number() over(partition by occupation order by name) as row_number
        from occupations
    ) as t
group by row_number
order by row_num