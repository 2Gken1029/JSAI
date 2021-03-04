#!python3
import MorphologicalAnalysis
import glob

file_list = glob.glob('../textFolder/allText/*.txt')

excel_sheet = '../wordTime_train.xlsx'
#excel_sheet = '../wordHigh_train.xlsx'

file_list.sort()

for path in file_list:
    print(str(path.split("/")[3]) + " , "+ str(MorphologicalAnalysis.main(path, excel_sheet)))