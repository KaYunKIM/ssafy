CREATE TABLE COUNTRIES(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_num TEXT NOT NULL,
    check_in TEXT NOT NULL,
    check_out TEXT NOT NULL,
    grade TEXT NOT NULL,
    price INTEGER NOT NULL
);



INSERT INTO COUNTRIES (room_num, check_in, check_out, grade, price) VALUES('B203', '2019-12-31', '2020-01-03', 'SUITE', 900);
INSERT INTO COUNTRIES (room_num, check_in, check_out, grade, price) VALUES('1102', '2020-01-04', '2020-01-08', 'SUITE', 850);
INSERT INTO COUNTRIES (room_num, check_in, check_out, grade, price) VALUES('303', '2020-01-01', '2020-01-03', 'DELUXE', 500);
INSERT INTO COUNTRIES (room_num, check_in, check_out, grade, price) VALUES('807', '2020-01-04', '2020-01-07', 'SUPERIOR', 300);


ALTER TABLE COUNTRIES RENAME TO HOTELS;


SELECT room_num, price FROM HOTELS ORDER BY price DESC LIMIT 2;


SELECT grade, COUNT(grade) FROM HOTELS GROUP BY grade ORDER BY COUNT(grade) DESC;


SELECT * FROM HOTELS WHERE (room_num LIKE 'B%') OR (grade='DELUXE');


SELECT room_num FROM HOTELS WHERE room_num NOT LIKE 'B%' AND check_in='2020-01-04' ORDER BY price;