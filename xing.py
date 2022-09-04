import pandas as pd
import numpy as np
import collections.abc

chaizi = pd.read_csv('chaizi_dict.csv')
chaizi['chaizi'] = chaizi['chaizi'].apply(eval)

bx = pd.read_csv('bushou_xiaozi_concat.csv', header=None, names=['zi', 'key'])

res = []
failed = []

def app(i):
    # 获得拆字的形状
    vv = i[1]
    # 获取到第一个的key
    key1 = bx[bx['zi'] == vv[0]]['key'].values[0]
    # 尝试获取第二个的key
    key2 = bx[bx['zi'] == vv[1]]['key'].values
    if len(key2) > 0:
        res.append([i[0], key1+key2])
        return None
    else:
        cz = chaizi[chaizi['zi'] == vv[1]]['chaizi'].values
        if len(cz) > 0 :
            cz=cz[0]
        else:
            failed.append([i[0],vv[1]])
            return key1+'`'
        key2 = bx[bx['zi'] == cz[0]]['key'].values[0]
        res.append([i[0], key1+key2])
        return None



chaizi.apply(app, axis=1)

rres = []
for i in res:
    if isinstance(i[1],np.ndarray):
        for j in i[1]:
            rres.append([i[0],j])
    else:
        rres.append([i[0],i[1]])

xing = pd.DataFrame(rres, columns=['zi', 'key'])

print(failed)
xing.drop_duplicates(inplace=True)
xing.to_csv('xing.csv', index=False)
