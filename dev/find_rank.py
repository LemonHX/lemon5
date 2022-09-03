import json
import pandas as pd
from pypinyin import Style, pinyin
from pypinyin.contrib.tone_convert import to_initials, to_finals


class FindRank:
    data = {}
    merged = None
    weight = {}
    initials_rank = {}
    finals_rank = {}

    def __init__(self):
        file = open("./dev/weight.json")
        file_str = file.read()
        self.weight = json.loads(file_str)
        self.add_all_data()
        return

    def add_data(self, path):
        self.data[path.split("/")[-1].split(".")[0]] = pd.read_csv(
            path, header=None, names=["word", "count"], sep='\\t', engine='python').dropna()

    def add_all_data(self):
        for (k, v) in self.weight.items():
            self.add_data("./dev/"+k+".txt")
            self.data[k]["count"] = self.data[k]["count"].map(
                lambda x: x * int(v) + 1)
            self.data[k]["count"] = self.data[k]["count"].astype('int')
        self.merged = pd.concat(self.data.values(), ignore_index=True)
        self.merged.dropna(inplace=True)
        self.merged.sort_values(by="count", ascending=False, inplace=True)
        i = 0
        for index, row in self.merged.iterrows():
            print("{}/{}".format(i, len(self.merged)))
            self.rank_by_pinyin(row['word'], row["count"])
            i += 1
        return

    def get_pinyin(self):
        self.merged_pinyin = self.merged["word"].map(lambda x: pinyin(x))

    def get_finals_rank(self):
        return {k: v for k, v in sorted(self.finals_rank.items(), reverse=True, key=lambda item: item[1])}

    def get_initials_rank(self):
        return {k: v for k, v in sorted(self.initials_rank.items(), reverse=True, key=lambda item: item[1])}

    def rank_by_pinyin(self, word, freq):
        pinyin_full = pinyin(word, style=Style.TONE3, heteronym=True)
        for arr in pinyin_full:
            for py in arr:
                ini = to_initials(py, strict=False)
                fin = to_finals(py, strict=False)
                if py[-1].isdigit():
                    if ini in self.initials_rank:
                        self.initials_rank[ini] += freq
                    else:
                        self.initials_rank[ini] = freq
                    if fin in self.finals_rank:
                        self.finals_rank[fin] += freq
                    else:
                        self.finals_rank[fin] = freq


fr = FindRank()
print("done")
res = {"initials": fr.get_initials_rank(), "finals": fr.get_finals_rank()}
with open("./dev/rank.json", "w") as outfile:
    json.dump(res, outfile, indent=2, ensure_ascii=False)
