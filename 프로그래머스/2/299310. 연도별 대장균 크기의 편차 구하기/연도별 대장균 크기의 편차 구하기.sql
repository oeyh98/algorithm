WITH MAX_DATA AS(
    SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR_MAX, MAX(SIZE_OF_COLONY) AS SIZE_OF_COLONY
    FROM ECOLI_DATA
    GROUP BY YEAR(DIFFERENTIATION_DATE)
)

SELECT YEAR(ED.DIFFERENTIATION_DATE) AS YEAR, (MD.SIZE_OF_COLONY - ED.SIZE_OF_COLONY) AS YEAR_DEV, ED.ID
FROM ECOLI_DATA AS ED, MAX_DATA AS MD
WHERE YEAR(ED.DIFFERENTIATION_DATE) = MD.YEAR_MAX
ORDER BY 1, 2