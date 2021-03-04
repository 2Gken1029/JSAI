#!python3

import xlrd
import pprint

# Excelシートから単語と共起値を辞書型として取得
def exel_to_dic(sheet_name, excel_sheet):
    wb = xlrd.open_workbook(excel_sheet)
    sheet = wb.sheet_by_name(sheet_name)

    col_word =  sheet.col_values(1)
    col_values = sheet.col_values(5)

    word_and_value = {}

    for word, value in zip(col_word, col_values):
        word_and_value[word] = int(value)
    
    return word_and_value

# リストに格納された変数を文字列として扱う
def get_var_names(vars):
    names=[]
    for var in vars:
        for k,v in globals().items():
            if id(v) == id(var):
                names.append(k)
    return names

# sheet_list = wb.sheet_names()

# variable_list = []

# for sheet in sheet_list: # シート数に応じて動的に辞書型を作成
#     exec('{} = {}'.format(sheet, exel_to_dic(sheet)))
#     exec('variable_list.append({})'.format(sheet))

# for variable_name, dic in zip(get_var_names(variable_list), variable_list):
#     print(variable_name + " : " + str(dic))
