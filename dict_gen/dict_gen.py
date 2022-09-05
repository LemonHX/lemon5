import asyncio
from pypinyin.contrib.tone_convert import to_initials, to_finals
from pypinyin import Style, pinyin
import opencc
import pandas as pd
import os
import sys
import inspect

sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe())))))


converter = opencc.OpenCC('t2s.json')
wuma = pd.read_csv('wuma.csv')

failed = []
ciku = []


def guize(ci):
    from transport import pinyin_trans, tone_trans
    py = pinyin(ci, style=Style.TONE3)
    yin = []
    for y in py:
        y = y[0]
        ini = to_initials(y, strict=False)
        fin = to_finals(y)
        if ini == "" and (len(fin) == 1 or len(fin) == 3):
            ini = fin
        if ini == "" and len(fin) == 2:
            ini = fin[0]
            fin = fin[1]
        ini = pinyin_trans(ini)
        fin = pinyin_trans(fin)
        ton = y[-1]
        ton = tone_trans(ton)
        yin.append([ini, fin, ton])
    if len(ci) == 1:
        z = wuma[wuma['zi'] == ci]["wuma"].values
        if len(z) > 0:
            ciku.append([ci, "".join(yin[0])+z[0][3:]])
        else:
            failed.append(ci)
    if len(ci) == 2:
        z1 = wuma[wuma['zi'] == ci[0]]["wuma"].values
        z2 = wuma[wuma['zi'] == ci[1]]["wuma"].values
        if len(z1) > 0 and len(z2) > 0:
            ciku.append([ci, "".join(yin[0][:2]+yin[1])])
        else:
            if len(z1) == 0:
                failed.append(ci[0])
            if len(z2) == 0:
                failed.append(ci[1])
    if len(ci) == 3:
        z1 = wuma[wuma['zi'] == ci[0]]["wuma"].values
        z2 = wuma[wuma['zi'] == ci[1]]["wuma"].values
        z3 = wuma[wuma['zi'] == ci[2]]["wuma"].values
        if len(z1) > 0 and len(z2) > 0 and len(z3) > 0:
            ciku.append([ci, yin[0][0]+yin[1][0]+"".join(yin[2])])
        else:
            if len(z1) == 0:
                failed.append(ci[0])
            if len(z2) == 0:
                failed.append(ci[1])
            if len(z3) == 0:
                failed.append(ci[2])
    if len(ci) >= 4:
        buffer = ""
        not_append = False
        for c in range(0, len(ci)):
            z = wuma[wuma['zi'] == ci[c]]["wuma"].values
            if len(z) > 0:
                buffer += yin[c][0]+yin[c][2]
            else:
                failed.append(ci[c])
                not_append = True
        if buffer != "" and not not_append:
            ciku.append([ci, buffer])


def background(f):
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, **kwargs)
    return wrapped


lines = []


@background
def calc(name, s):
    i = 0
    for line in s:
        if i % 100 == 0:
            print(f"{name} {i}/{len(s)}")
        i += 1
        line = line.strip()
        line = converter.convert(line)
        guize(line)


def ssplit(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))


if __name__ == "__main__":
    path = sys.argv[1]
    export_path = path+".dict.csv"
    from_pos = int(sys.argv[2])
    i = from_pos
    to_pos = int(sys.argv[3])
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()[from_pos:to_pos]
        chunks = list(ssplit(lines, 8))
        loop = asyncio.get_event_loop()
        looper = asyncio.gather(
            *[calc(f"thread {i}:", chunks[i]) for i in range(0, 8)])
        results = loop.run_until_complete(looper)
    print("writing to file...")
    with open(export_path, 'a', encoding='utf-8') as f:
        for c in ciku:
            f.write(c[0]+","+c[1]+"\n")
    failed = pd.DataFrame(failed, columns=["zi"])
    failed.drop_duplicates(inplace=True)
    failed.to_csv(path+".failed.csv", index=False)
