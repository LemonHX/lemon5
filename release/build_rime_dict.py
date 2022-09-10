import pandas as pd

danzi = open("jianma.danzi.csv").readlines()[1:]
erzi = open("jianma.erzi.csv").readlines()[1:]
wuma = open("wuma.csv").readlines()[1:]
default_dict = open("./generated_dict/default.txt.dict.csv").readlines()

with open("./release/lemon5_dict.dict.yaml", "w") as f:
    f.write("""
---
name: lemon5_dict
version: "v0.2"
sort: original
use_preset_vocabulary: false
...
""")
    for l in danzi + erzi + wuma + default_dict:
        f.write(l.replace(",", "\t").replace(".0", ""))

with open("./release/lemon5_reverse.dict.yaml", "w") as g:
    g.write("""
---
name: lemon5_reverse
version: "v0.2"
sort: original
use_preset_vocabulary: false
...
""")
    fancha = open("fancha.csv").readlines()[1:]
    for j in fancha:
        g.write(j.replace(",", "\t").replace(".0", ""))
