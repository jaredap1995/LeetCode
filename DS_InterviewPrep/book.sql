DROP TABLE IF EXISTS books;
CREATE TABLE books(
    id serial primary key,
    author varchar(30),
    book varchar(30),
    year INT,
    genre varchar(30),
    copies_sold INT
);

\copy books (author, book, year, genre, copies_sold) from '/Users/jaredperez/Documents/LeetCode/DS_InterviewPrep/sample_bo
ok_data.csv' WITH CSV DELIMITER ',' HEADER;

-- write an SQL query to show the top 3 authors who sold the most books in total.

select author, copies_sold from books 
order by copies_sold desc
limit 3;


----
DROP TABLE IF EXISTS data;
CREATE TABLE data(
    id serial primary key,
    author_name varchar(30),
    book varchar(30),
    year INT,
    genre varchar(30),
    copies_sold INT
);

DROP TABLE IF EXISTS books;
CREATE TABLE books(
    id serial primary key,
    book_name varchar(30)
);

Insert into books (book_name)
select distinct book from data;

DROP TABLE IF EXISTS authors;
CREATE TABLE authors(
    id serial primary key,
    author varchar(30),
    book_id int REFERENCES books(id) ON DELETE CASCADE
);


INSERT INTO authors (author, book_id)
SELECT DISTINCT d.author_name, b.id FROM data d
JOIN books b ON b.book_name = d.book;

-- List Authors and Their Total Books Sold
select a.author, sum(d.copies_sold) from authors a
join books b on b.id = a.book_id
join data d on d.book = b.book_name
GROUP BY a.author;


-- List authors, copies sold for each book
select a.author, sum(d.copies_sold) , b.book_name from data d
join books b on d.book = b.book_name
join authors a on d.author_name = a.author
GROUP BY a.author, b.book_name;




