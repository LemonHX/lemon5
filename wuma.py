import pandas as pd
from transport import *
import sqlite3
from transport import *
not_applicatable = []

con = sqlite3.connect('wenshu.sqlite')
df = pd.read_sql_query("SELECT * FROM ZI_MAPPING_XU", con)

wuma = []
df0 = df[df["XU"] == 0]
df1 = df[df["XU"] == 1][["ZI","MAPPING"]]
def gen_df_one(row):
    if row[2] != "er" and row[1] != '':
        shengmu_trans = pinyin_trans(row[1])
        yunmu_trans = pinyin_trans(row[2])
    elif row[2] == "er":
        shengmu_trans = "e"
        yunmu_trans = "r"
    elif row[1] == "":
        yunmu_trans = pinyin_trans(row[2])
        if len(row[2]) == 2:
            shengmu_trans = row[2][0]
            yunmu_trans = row[2][1]
        else:
            shengmu_trans = yunmu_trans
    tone = tone_trans(str(row[3]))
    wuma.append([row[0], shengmu_trans+yunmu_trans+tone+"["+"``"])
df_one = df0[~(df0["ZI"].isin(df1["ZI"]))]
df_one.apply(gen_df_one, axis=1)
df1.columns = ["ZI","MAPPING1"]
df01 = df0.merge(df1, how="inner", on="ZI").drop("XU", axis=1)
df01 = df01[df01["YUNMU"] != ""]
def gen_wuma(row):
    if row[2] != "er" and row[1] != '':
        shengmu_trans = pinyin_trans(row[1])
        yunmu_trans = pinyin_trans(row[2])
    elif row[2] == "er":
        shengmu_trans = "e"
        yunmu_trans = "r"
    elif row[1] == "":
        yunmu_trans = pinyin_trans(row[2])
        if len(row[2]) == 2:
            shengmu_trans = row[2][0]
            yunmu_trans = row[2][1]
        else:
            shengmu_trans = yunmu_trans
    tone = tone_trans(str(row[3]))
    wuma.append([row[0], shengmu_trans+yunmu_trans+tone+"["+row[4]+row[5]])
df01.apply(gen_wuma,axis=1)
wuma = pd.DataFrame(wuma,columns=["zi","wuma"])
wuma.drop_duplicates(inplace=True)
wuma.to_csv("wuma.csv",index=False)

fancha = []
def int_to_bool_list(num):
    return [bool(num & (1<<n)) for n in range(5)]
def gen_fancha(row):
    for i in range(0,32):
        mask = int_to_bool_list(i)
        wuma = row[1]
        wuma = wuma.replace("[","")
        res = ""
        for j in range(0,5):
            if mask[j]:
                res += wuma[j]
            else:
                res += "`"
        res = res[0]+res[1]+res[2]+"["+res[3]+res[4]
        fancha.append([row[0],res])
wuma.apply(gen_fancha,axis=1)
fancha = pd.DataFrame(fancha,columns=["zi","fancha"])
fancha.drop_duplicates(inplace=True)
fancha.to_csv("fancha.csv",index=False)