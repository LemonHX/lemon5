import pandas as pd
import opencc

converter = opencc.OpenCC('t2s.json')

wuma = pd.read_csv('wuma.csv')
not_covered = []
for c in range(0x4e00, 0x9fa6):
    cc = chr(c)
    cc = converter.convert(cc)
    if cc not in wuma['zi'].values:
        not_covered.append(cc)

print(not_covered)
open("wuma_not_covered.txt", "w").write("\n".join(not_covered))