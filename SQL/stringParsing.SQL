CREATE TABLE names(
    id serial primary key, 
    full_name varchar(200)
);

SELECT SUBSTR(
    full_name, 1, position('' IN full_name)-1)
    AS first_name from names;