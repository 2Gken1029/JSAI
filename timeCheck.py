#!python3

import glob
import os,re
import mojimoji

file_list = glob.glob('nucc/*.txt')
file_list.sort()

text_time = {}

for textFile in file_list:
    with open(textFile) as f:
        text = f.readlines()
        text_time[textFile.split("/")[1]] = (text[0].split("（")[1]).split("）")[0]


for k, v in text_time.items():
    print(k + " , " + str(int(re.sub("\\D", "", mojimoji.zen_to_han(v)))*60)) # ファイル名 , 秒数
