import json

trans = json.load(open("transport.json", "r"))
def pinyin_trans(pinyin):
    if pinyin in trans["pinyin"].keys():
        return trans["pinyin"][pinyin]
    elif len(pinyin) == 1:
        return pinyin
    else:
        raise ValueError(pinyin + "not in json")


def tone_trans(tone):
    if tone in trans["tone"].keys():
        return trans["tone"][tone]
    else:
        return "b"

if __name__ == "__main__":
    import sys
    from pypinyin.contrib.tone_convert import to_initials, to_finals
    py = sys.argv[1]
    if py == "-h":
        print("Usage: python3 transport.py [pinyin]")
        print("Example: python3 transport.py hao3")
        exit(0)
    ini = to_initials(py, strict=False)
    fin = to_finals(py)
    tone = py[-1]
    print(f"{pinyin_trans(ini)+pinyin_trans(fin)+tone_trans(tone)}")

    