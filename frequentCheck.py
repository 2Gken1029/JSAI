#!python3

import MeCab
import sys, os, collections, glob

def morphologicalAnalysis(textFile): # 形態素解析

    with open(textFile) as f:
        text = f.readlines()

    mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    mecab.parse('')

    # リスト内文字列の"\n"を削除
    text = [s.replace('\n', '') for s in text]

    morphologicalAnalysis = []

    for s in text:
        node = mecab.parseToNode(s)
        while node:
            # 原型に変換
            morphologicalAnalysis.append(node.feature.split(",")[6])
            node = node.next

    # 「*」を取り除く
    morphologicalAnalysis = [item for item in morphologicalAnalysis if item != "*"]

    return morphologicalAnalysis

path_key = 'keyword.txt'
morphologicalAnalysis_key = morphologicalAnalysis(path_key)

file_list = glob.glob('../textFolder/sampleText/*.txt')
file_list.sort()
for file in file_list:
    duplicates = set(morphologicalAnalysis_key) & set(morphologicalAnalysis(file))
    print(str(file.split("/")[3]) + " , "+ str(len(duplicates)))

### デバック用 ###
# print(morphologicalAnalysis)
# for word in morphologicalAnalysis:
#     print(word)
# for k, v in collections.Counter(morphologicalAnalysis).most_common():
#     print(k + " : " + str(v))