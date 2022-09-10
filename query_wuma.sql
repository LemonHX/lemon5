SELECT
    WUMA.ZI,
    WUMA.WUMA,
    CAST(POW(0.5, IFNULL(ZIPIN.PINLV, 6) - 1) * 100 AS INT) AS PINLV
FROM WUMA
LEFT JOIN ZIPIN ON WUMA.ZI = ZIPIN.ZI;