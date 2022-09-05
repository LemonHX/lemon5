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

    