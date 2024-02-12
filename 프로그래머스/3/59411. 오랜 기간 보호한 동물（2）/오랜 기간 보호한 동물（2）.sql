SELECT i.ANIMAL_ID, i.NAME
FROM ANIMAL_INS as i
join ANIMAL_OUTS as o
on i.ANIMAL_ID = o.ANIMAL_ID
order by timestampdiff(day, o.DATETIME, i.DATETIME)
limit 2