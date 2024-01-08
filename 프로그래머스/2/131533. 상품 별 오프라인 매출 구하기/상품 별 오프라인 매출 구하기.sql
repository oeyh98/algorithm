-- 코드를 입력하세요
SELECT p.PRODUCT_CODE, sum(p.PRICE*o.SALES_AMOUNT) as SALES
from PRODUCT as p
join OFFLINE_SALE as o
on p.PRODUCT_ID = o.PRODUCT_ID
group by o.PRODUCT_ID
order by 2 desc, 1 asc