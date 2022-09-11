import pandas as pd
import os
import zipfile

version = open("VERSION").read()

def zipdir(dirPath=None, zipFilePath=None, includeDirInZip=True):
    if not zipFilePath:
        zipFilePath = dirPath + ".zip"
    if not os.path.isdir(dirPath):
        raise OSError("dirPath argument must point to a directory. "
            "'%s' does not." % dirPath)
    parentDir, dirToZip = os.path.split(dirPath)
    def trimPath(path):
        archivePath = path.replace(parentDir, "", 1)
        if parentDir:
            archivePath = archivePath.replace(os.path.sep, "", 1)
        if not includeDirInZip:
            archivePath = archivePath.replace(dirToZip + os.path.sep, "", 1)
        return os.path.normcase(archivePath)
    outFile = zipfile.ZipFile(zipFilePath, "w",
        compression=zipfile.ZIP_DEFLATED)
    for (archiveDirPath, dirNames, fileNames) in os.walk(dirPath):
        for fileName in fileNames:
            filePath = os.path.join(archiveDirPath, fileName)
            outFile.write(filePath, trimPath(filePath))
        if not fileNames and not dirNames:
            zipInfo = zipfile.ZipInfo(trimPath(archiveDirPath) + "/")
            outFile.writestr(zipInfo, "")
    outFile.close()


danzi = open("jianma.danzi.csv").readlines()[1:]
erzi = open("jianma.erzi.csv").readlines()[1:]
sanzi = open("jianma.sanzi.csv").readlines()[1:]
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
    for l in danzi + erzi + sanzi + wuma + default_dict:
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

zipdir("release", f"./RIME_Lemon5.{version}.zip")
