#!python3

import MeCab
import pyfpgrowth
import xlrd
import sys, os, pprint, collections, glob
import xlsxDictionary, scoreCheck

def main(path, excel_sheet):

    mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

    with open(path) as f:
        text = f.readlines()

    # リスト内文字列の"\n"を削除
    text = [s.replace('\n', '') for s in text]

    mecab.parse('')

    morphologicalAnalysis_list = []

    for s in text:
        morphologicalAnalysis = []
        node = mecab.parseToNode(s)
        while node:
            # 原型に変換
            morphologicalAnalysis.append(node.feature.split(",")[6])
            node = node.next
        morphologicalAnalysis_list.append(morphologicalAnalysis)


    wb = xlrd.open_workbook(excel_sheet)
    sheet_list = wb.sheet_names()

    variable_list = []

    for sheet in sheet_list: # シート数に応じて動的に辞書型を作成
        exec('{} = {}'.format(sheet, xlsxDictionary.exel_to_dic(sheet, excel_sheet)))
        exec('variable_list.append({})'.format(sheet))


    # ["今日","すぐ","今回","今"]の辞書内容
    # for variable_name, dic in zip(xlsxDictionary.get_var_names(variable_list), variable_list):
    #     print(variable_name + " : " + str(dic))

    return sum(scoreCheck.counterMethod(morphologicalAnalysis_list, variable_list, excel_sheet))