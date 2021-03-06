CREATE TABLE flights(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    flight_num TEXT NOT NULL,
    departure TEXT NOT NULL,
    waypoint TEXT NOT NULL,
    arrival TEXT NOT NULL,
    price INTEGER NOT NULL
);


INSERT INTO flights (flight_num, departure, waypoint, arrival, price) VALUES('RT9122','MADRID', 'BEIJING', 'INCHEON', 200);
INSERT INTO flights (flight_num, departure, waypoint, arrival, price) VALUES('XZ0352', 'LA', 'MOSCOW', 'INCHEON', 800);
INSERT INTO flights (flight_num, departure, waypoint, arrival, price) VALUES('SQ0972', 'LONDON', 'BEIJING', 'SYDNEY', 500);


SELECT * FROM FLIGHTS;


SELECT WAYPOINT FROM FLIGHTS;


SELECT ID, FLIGHT_NUM  FROM FLIGHTS WHERE PRICE<600;


SELECT DEPARTURE FROM FLIGHTS WHERE ARRIVAL='INCHEON' AND PRICE>=500;


SELECT ID, FLIGHT_NUM FROM FLIGHTS WHERE FLIGHT_NUM LIKE '__0__2' AND WAYPOINT='BEIJING';


UPDATE FLIGHTS SET WAYPOINT='TOKYO' WHERE FLIGHT_NUM='SQ0972';


DELETE FROM FLIGHTS WHERE FLIGHT_NUM='RT9122';