#! python3
# countCode.py - 引数で指定したテキストファイルの単語数を調べる

import sys, os, glob

file_list = glob.glob('textFolder/testText/*.txt')
file_list.sort()

def remove(string_list):
    # リスト内文字列の特定文字を削除
    string_list = [s.replace('\n', '') for s in string_list]
    string_list = [s.replace('、', '') for s in string_list]
    string_list = [s.replace('。', '') for s in string_list]
    return string_list

for textFile in file_list:
    with open(textFile) as f:
        string_list = f.readlines()
        # リスト内文字列を全て結合
        word_all = ''.join(remove(string_list))
        print(textFile.split("/")[2] + " , " + str(len(word_all)))