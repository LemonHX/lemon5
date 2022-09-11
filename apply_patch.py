wuma = open("wuma.csv").readlines()
wuma_patch = open("wuma.patch.csv").readlines()
wuma += wuma_patch
open("wuma.csv", "w").writelines(wuma)
