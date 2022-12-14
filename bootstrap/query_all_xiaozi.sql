-- all xiaozi
SELECT CHAIZI.CHAI,BIHUA.BIHUA, PINYIN.SHENGMU, PINYIN.YUNMU, COUNT(CHAIZI.ZI) AS USED 
FROM CHAIZI
LEFT JOIN BIHUA ON CHAIZI.CHAI = BIHUA.ZI
LEFT JOIN KEY_MAPPING ON CHAIZI.ZI = KEY_MAPPING.ZI
LEFT JOIN PINYIN ON PINYIN.ZI = CHAIZI.CHAI
WHERE 
    CHAIZI.CHAI NOT IN (SELECT ZI FROM KEY_MAPPING)
GROUP BY CHAIZI.CHAI, PINYIN.SHENGMU, PINYIN.YUNMU, PINYIN.DIAO
ORDER BY BIHUA.BIHUA;
