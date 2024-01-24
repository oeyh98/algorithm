SELECT i.NAME, i.DATETIME 
from ANIMAL_INS as i
left join ANIMAL_OUTS as o
on i.ANIMAL_ID = o.ANIMAL_ID
where o.ANIMAL_ID is NULL
order by DATETIME asc 
limit 3
