-- 코드를 입력하세요
SELECT MCDP_CD AS 진료과코드, COUNT(APNT_YMD) as 5월예약건수
FROM APPOINTMENT
WHERE DATE_FORMAT(APNT_YMD, '%Y-%m') = '2022-05'
GROUP BY MCDP_CD
order by 5월예약건수 asc, 진료과코드 asc

