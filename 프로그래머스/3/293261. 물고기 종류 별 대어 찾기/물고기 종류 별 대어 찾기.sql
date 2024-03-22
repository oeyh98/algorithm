SELECT ID, FISH_NAME, LENGTH
FROM FISH_INFO
JOIN FISH_NAME_INFO
USING(FISH_TYPE)
WHERE FISH_TYPE, LENGTH = (
    SELECT FISH_TYPE, MAX(LENGTH)
    FROM FISH_INFO
    GROUP BY FISH_TYPE
)