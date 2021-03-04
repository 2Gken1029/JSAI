#! python3
# countCode.py - 引数で指定したテキストファイルの単語数を調べる

import sys, os, glob

file_list = glob.glob('hiragana_ver/*.txt')
file_list.sort()

for file in file_list:
    with open(file) as f:
        string_list = f.readlines()
    # リスト内文字列の特定文字を削除
    string_list = [s.replace('-', '') for s in string_list]
    string_list = [s.replace('\n', '') for s in string_list]
    string_list = [s.replace('、', '') for s in string_list]
    string_list = [s.replace('。', '') for s in string_list]
    string_list = [s.replace('？', '') for s in string_list]
    string_list = [s.replace('?', '') for s in string_list]
    string_list = [s.replace('ゃ', '') for s in string_list]
    string_list = [s.replace('ゅ', '') for s in string_list]
    string_list = [s.replace('ょ', '') for s in string_list]
    # リスト内文字列を全て結合
    word_all = ''.join(string_list)
    print(file.split("/")[1] + " , " + str(len(word_all)))