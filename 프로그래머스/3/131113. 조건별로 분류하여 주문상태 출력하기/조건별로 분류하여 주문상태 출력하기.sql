-- 코드를 입력하세요
SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE, '%Y-%m-%d') AS OUT_DATE, 
    case
        when OUT_DATE is null then '출고미정'
        when concat(substr(OUT_DATE, 6, 2), substr(OUT_DATE, 9, 2)) <= 0501 Then '출고완료'
        else '출고대기'
        end
        as 출고여부
from FOOD_ORDER
order by 1


