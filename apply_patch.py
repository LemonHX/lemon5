xiaozi = open("xiaozi_key_mapping.csv").readlines()
xiaozi_patch = open("xiaozi_key_mapping.patch.csv").readlines()
xiaozi += xiaozi_patch

bushou = open("bushou_key_mapping.csv").readlines()
bushou_xiaozi_concat = bushou[1:] + xiaozi[1:]
open("bushou_xiaozi_concat.csv", "w").writelines(bushou_xiaozi_concat)

wuma = open("wuma.csv").readlines()
wuma_patch = open("wuma.patch.csv").readlines()
wuma += wuma_patch
open("wuma.csv", "w").writelines(wuma)