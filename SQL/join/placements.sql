select name from (
    select f.id, name, f.friend_id, p.salary as friend_salary
    from friends f
    left join packages p on f.friend_id = p.id --friends salary
    left join students s on s.id = f.id
    left join packages o on f.id = p.id ---students salary
    where o.salary < p.salary --This comparison is valid because they are essentialy the salary of two different students, current student, and students friend
) cte order by friend_salary asc;