import pandas as pd

bushou = pd.read_csv('bushou_key_mapping.csv')
bushous = bushou['bushou'].tolist()


chaizi = pd.read_csv('chaizi_dict.csv')
chaizi['chaizi'] = chaizi['chaizi'].apply(eval)

all_word = pd.read_csv('all_word.csv')


xiaozi = set()

def collect_xiaozi(arr):
    if arr[0] in bushous:
        return arr
    else:
        xiaozi.add(arr[0])



# 拆字的第一个字都应该是小字（我自己看了一眼）
chaizi['chaizi'].apply(collect_xiaozi)
xiaozi = list(xiaozi)
def sort_xiaozi_cmp(xiaozi):
    vs = all_word[all_word['zi'] == xiaozi]['index'].values
    if len(vs) > 0:
        return vs[0]
    else:
        print("{} 没找到".format(xiaozi))
        return 999999

xiaozi = sorted(xiaozi, key=sort_xiaozi_cmp)
f = open('xiaozi.txt', 'w')

for i in xiaozi:
    init = all_word[all_word['zi'] == i]['ini'].values
    if len(init) > 0:
        for ini in init:
            if ini == "zh":
                ini = 'i'
            if ini == "sh":
                ini = 'u'
            if ini == "ch":
                ini = 'v'
            f.write("{},{}\n".format(i,ini))

# 然后再用pandas自己看着洗洗