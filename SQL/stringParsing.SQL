CREATE TABLE names(
    id serial primary key, 
    full_name varchar(200)
);

-- First Name
SELECT SUBSTR(
    full_name, 1, position('' IN full_name)-1)
    AS first_name from names;

-- Middle Name
select substr(
    full_name, 
)