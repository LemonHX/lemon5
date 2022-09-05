# 柠檬五码

柠檬五码是自由的舒适的全新输入法方案，
是经柠檬群讨论并实现的兼具人体工程学和准确度的双拼方案，柠檬五码得名于其中任何字的全码都是五码。


# 单字全码
正常情况下可以省略 `[` 符号

| 单字 | 双拼       | 音调  | 双形        | 全码   |
| ---- | ---------- | ----- | ----------- | ------ |
| 柠   | NK（ning） | G (á) | MB （木宀） | NKG[MB |
| 檬   | MR（meng） | G (á) | MC （木艹） | MRG[MC |
| 五   | WU（wu）   | H (ǎ) | AA （一一） | WUH[AA |
| 码   | MA（ma）   | H (ǎ) | UM （石马） | MAH[UM |

# 使用规则
柠檬五码是整句输入法，和小鹤不同，柠檬五码有一个缓冲区可供描述每个字的采用

柠檬五码使用空格来分割句子在空格后空格即为将当前内容写出

`[` 键输入后描述当前双拼字的形状，正常情况下键入双拼和音调就可以，无需补全形状，形状用于去重码

`` ` ``（grave）键位通配键盘，可以充当声母韵母音调或者是双形中的任意字符。
理论上`` ` `` `` ` `` `` ` `` `` ` `` `` ` `` 能表示任意字符


## 盲打模式
好啦，我知道你们喜欢盲打，那么盲打模式就是这样的

| 字数 | 规则                               | 例词     | 全码                             |
| ---- | ---------------------------------- | -------- | -------------------------------- |
| 1    | 全码无形                           | 啊       | AAF （只有一个韵母的词重复两次） |
| 1    | 全码                               | 哦       | WOHKW                            |
| 2    | 首字前两码 + 末字前两码 + 末字读音 | 柠檬     | NKMRG                            |
| 3    | 前两字首码 + 末字前两码 + 末字读音 | 输入法   | URFAH                            |
| 4+   | （辅音+读音）* N个字               | 一个顶俩 | YFGJDHLH                         |

# 关于词典
柠檬水平有限，从网上随便爬了点词做的默认词典，如果嫌不够可以自制

自制词典只需要一个只有字和`\n`的文件，然后使用

```sh
python ./dict_gen/dict_gen.py 开始行数 结束行数
```
或者你可以使用 [深蓝词库转换](https://github.com/studyzy/imewlconverter) 下载一些其他输入法的词库，转换为 rime 格式然后再使用regex `\t.*$` 剔除掉他们的拼音并保存成上述格式然后跑上方的脚本~

脚本会导出`*.dict.csv`和`*.failed.csv`, 记得查看`failed.csv`如果有关键常用字形缺失请联系我哦~

# License
- chaizi_dict: [署名3.0](http://creativecommons.org/licenses/by/3.0/deed.zh_TW) [项目地址](https://github.com/kfcd/chaizi)
- THUOCL: [license](./dev/LICENSE)