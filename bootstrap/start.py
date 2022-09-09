import sqlite3
import pandas as pd
import sys
import os
import inspect
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe())))))

# 建表
con = sqlite3.connect('wenshu.sqlite')
con.executescript(open("./bootstrap/create_table.sql").read())

# 部首
df = pd.read_csv("./bootstrap/bushou_key_mapping.csv")
data = tuple(df.itertuples(index=True))
wildcards = ','.join(['?'] * len(data[0]))
insert_sql = 'INSERT INTO KEY_MAPPING VALUES(%s)' % wildcards
con.executemany(insert_sql, data)
con.commit()


# 小字
from transport import *
con = sqlite3.connect('wenshu.sqlite')
df = pd.read_sql_query(open("./bootstrap/query_all_xiaozi.sql").read(), con)
def k(x):
    try:
        if x[1] == "er":
            return "e"
        if x[0] == "":
            return pinyin_trans(x[1])
        else:
            return pinyin_trans(x[0])
    except:
        return "`"
df["SHENGMU"] = df[["SHENGMU", "YUNMU"]].apply(k, axis=1)
df.drop(columns=['BIHUA','USED', 'YUNMU'], inplace=True)
df.rename(columns={"SHENGMU":"KEY"}, inplace=True)
df.to_csv("./bootstrap/all_xiaozi.csv", index=False)
df.index = np.arange(len(data), len(data)+len(df))
data = tuple(df.itertuples(index=True))
wildcards = ','.join(['?'] * len(data[0]))
insert_sql = 'INSERT INTO KEY_MAPPING VALUES(%s)' % wildcards
con.executemany(insert_sql, data)
con.commit()

# create view for zi mapping
con.executescript(open("./bootstrap/wuma.view.sql").read())
con.close()
