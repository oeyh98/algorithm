-- 코드를 입력하세요
SELECT EXTRACT(hour from DATETIME) as HOUR, count(*) as COUNT
from ANIMAL_OUTS
where EXTRACT(hour from DATETIME) > 8 and EXTRACT(hour from DATETIME) < 20
group by EXTRACT(hour from DATETIME)
order by HOUR asc