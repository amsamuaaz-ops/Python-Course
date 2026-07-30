

CREATE TABLE IF NOT EXISTS book (

book_id INTEGER PRIMARY KEY,

title TEXT NOT NULL,

genre TEXT NOT NULL,

rating REAL NOT NULL,

pages INTEGER NOT NULL,

pub_year INTEGER NOT NULL

);

INSERT INTO book VALUES (1, 'Dragon Quest', 'Fantasy', 9.2, 312, 2021);

INSERT INTO book VALUES (2, 'Code Wizards', 'Sci-Fi', 8.5, 280, 2020);

INSERT INTO book VALUES (3, 'Ocean Deep', 'Adventure', 7.8, 195, 2022);

INSERT INTO book VALUES (4, 'Star Rangers', 'Sci-Fi', 9.5, 340, 2019);

INSERT INTO book VALUES (5, 'Forest Secrets', 'Fantasy', 8.1, 228, 2023);

INSERT INTO book VALUES (6, 'Robot City', 'Sci-Fi', 7.2, 260, 2021);

INSERT INTO book VALUES (7, 'Time Jumpers', 'Adventure', 8.9, 175, 2022);

INSERT INTO book VALUES (8, 'Magic Academy', 'Fantasy', 9.0, 398, 2020);

SELECT title,rating FROM book ORDER BY rating ASC;
SELECT title,rating FROM book ORDER BY rating DESC;
SELECT title,rating FROM book ORDER BY rating DESC LIMIT 3;
SELECT title,pub_year FROM book ORDER BY pub_year ASC LIMIT 5;
SELECT genre,COUNT(*)AS book_count FROM book GROUP BY genre;
SELECT genre,
        SUM(pages) AS total_pages,
        AVG(rating) AS avrg_rating FROM book GROUP BY genre;

SELECT genre,COUNT(*) AS book_count FROM book GROUP BY genre HAVING COUNT(*) >2;

SELECT genre,AVG(rating) AS book_AVG FROM book GROUP BY genre HAVING AVG(rating) >8.5;
