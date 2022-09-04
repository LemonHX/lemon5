import pandas as pd

xing = pd.read_csv('xing.csv')
all_word = pd.read_csv('all_word.csv')

quan = all_word.merge(xing, on='zi', how='right')
quan.dropna(inplace=True)


def pinyin_trans(pinyin):
    if pinyin == "iao":
        return "q"
    if pinyin == "en":
        return "w"
    if pinyin == "eng" or pinyin == "uan":
        return "r"
    if pinyin == "ue" or pinyin == "ve":
        return "t"
    if pinyin == "un":
        return "y"
    if pinyin == "uo":
        return "u"
    if pinyin == "ou":
        return "o"
    if pinyin == "ie":
        return "p"
    if pinyin == "uang":
        return "s"
    if pinyin == "ai":
        return "d"
    if pinyin == "an":
        return "f"
    if pinyin == "ang":
        return "g"
    if pinyin == "ao":
        return "h"
    if pinyin == "ian":
        return "j"
    if pinyin == "ing" or pinyin == "uai":
        return "k"
    if pinyin == "in":
        return "l"
    if pinyin == "ei":
        return "z"
    if pinyin == "ia":
        return "x"
    if pinyin == "ua":
        return "c"
    if pinyin == "ui":
        return "v"
    if pinyin == "iu":
        return "b"
    if pinyin == "ong" or pinyin == "iong":
        return "n"
    if pinyin == "iang":
        return "m"
    if pinyin == "zh":
        return "i"
    if pinyin == "ch":
        return "v"
    if pinyin == "sh":
        return "u"
    return pinyin


def tone_trans(tone):
    if tone == "1":
        return "f"
    if tone == "2":
        return "g"
    if tone == "3":
        return "h"
    if tone == "4":
        return "j"
    return "b"


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
