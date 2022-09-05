import pandas as pd
from transport import *

xing = pd.read_csv('xing.csv')
all_word = pd.read_csv('all_word.csv')

quan = all_word.merge(xing, on='zi', how='right')
quan.dropna(inplace=True)



quan['ini'] = quan['ini'].apply(pinyin_trans)
quan['fin'] = quan['fin'].apply(pinyin_trans)
quan["tone"] = quan["tone"].apply(tone_trans)
wuma = []
quan.apply(lambda x: wuma.append([x[0], x[2]+x[3]+x[4]+x[5]]), axis=1)
wuma = pd.DataFrame(wuma, columns=["zi", "wuma"]).drop_duplicates()


wuma.to_csv(
    "wuma.csv", index=False)


chongma = wuma[wuma.duplicated(subset=["wuma"], keep=False)].sort_values("wuma")
unique = pd.DataFrame(wuma["zi"].unique(), columns=["zi"])
unique_and_chongma = chongma.drop(chongma[~(chongma["zi"].isin(unique["zi"]))].index)

unique_and_chongma.to_csv("wuma_chongma.csv", index=False)
