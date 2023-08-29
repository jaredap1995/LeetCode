-- You are given a table, Projects, containing three columns: Task_ID, Start_Date and End_Date. It is guaranteed that the difference between the End_Date and the Start_Date is equal to 1 day for each row in the table.
-- If the End_Date of the tasks are consecutive, then they are part of the same project. Samantha is interested in finding the total number of different projects completed.
-- Write a query to output the start and end dates of projects listed by the number of days it took to complete the project in ascending order. If there is more than one project that have the same number of completion days, then order by the start date of the project.


--We need to know start dates that dont exist in end date
with s_cte as (
    select start_date as start_date,
    row_number() over (order by start_date) as row_start
    from projects
    where start_date not in (select end_date from projects)
), ---and end_dates that dont exist in start_date
e_cte as (
    select end_date as end_date,
    row_number() over (order by end_date) as row_end
    from projects 
    where end_date not in (select start_date from projects)
)
select start_date,
end_date from s_cte
join e_cte on s_cte.row_start = e_cte.row_end
order by (end_date - start_date), start_date



--Use row number to uniquely identify each of these values as the start and end



---join them on row_number


-- order by length or project and start date if length is equal