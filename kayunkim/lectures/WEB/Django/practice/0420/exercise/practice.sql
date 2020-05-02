-- CREATE - 데이터 생성
CREATE TABLE classmates(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
);

-- DROP -테이블 삭제
DROP TABLE classmates;

-- SELECT -데이터 조회
SELECT * FROM classmates;

-- INSERT - 데이터 삽입
INSERT INTO classmates (name,age) VALUES('구동엽', 20);
INSERT INTO classmates (name,age) VALUES('김가윤', 19);
INSERT INTO classmates (name,age) VALUES('최동녘', 18);
INSERT INTO classmates (name,age) VALUES('김정원', 17);
INSERT INTO classmates (name,age) VALUES('박선영', 16);


INSERT INTO classmates VALUES(6, '구동엽', 100);

-- SELECT - 데이터 조회
SELECT name FROM classmates;
SELECT name, age FROM classmates;

-- LIMIT -개수 조정
SELECT * FROM classmates LIMIT 1;

-- OFFSET -위에서부터 떨어진다 +1부터 가져오기
SELECT * FROM classmates LIMIT 1 OFFSET 2;

-- DISTINCT
INSERT INTO classmates (name) VALUES('김정원'):
SELECT DISTINCT name FROM classmates;

-- DELETE 데이터 삭제
DELETE FROM classmates WHRER id = 1;

-- UPDATE - 수정하기
UPDATE classmates SET name = '김가든' WHERE id = 3;

-- WHERE
SELECT * FROM classmates WHERE name = '김가든' AND age = 20;

-- COUNT,AVG,MAX
SELECT COUNT(*) FROM classmates;
SELECT max(age) FROM classmates;
SELECT AVG(age) FROM classmates;

-- LIKE(%, _)
SELECT * FROM classmates WHERE name LIKE '김%';
SELECT * FROM classmates WHERE name LIKE '%엽';
SELECT * FROM classmates WHERE age LIKE '2_';

-- ORDER BY - 정렬기능
SELECT * FROM classmates ORDER BY age ASC;
SELECT * FROM classmates ORDER BY age DESC;
