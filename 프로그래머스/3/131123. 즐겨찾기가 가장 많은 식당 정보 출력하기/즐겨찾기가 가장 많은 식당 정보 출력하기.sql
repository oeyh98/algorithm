SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO
where (FOOD_TYPE, FAVORITES) in 
       (select FOOD_TYPE, max(FAVORITES)
      from REST_INFO
      group by FOOD_TYPE)
group by FOOD_TYPE
order by 1 desc