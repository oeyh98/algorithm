-- 코드를 입력하세요
SELECT MONTH(START_DATE) as MONTH, CAR_ID, count(HISTORY_ID) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where CAR_ID in(SELECT CAR_ID
                from CAR_RENTAL_COMPANY_RENTAL_HISTORY
                where MONTH(START_DATE) BETWEEN 8 AND 10
                group by CAR_ID
                having count(HISTORY_ID) > 4
               ) and MONTH(START_DATE) BETWEEN 8 AND 10
group by MONTH, CAR_ID
having count(HISTORY_ID) > 0
order by 1 asc, 2 desc

