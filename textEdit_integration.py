#!python3

import glob

read_files = glob.glob('textFolder/trainingText/*.txt')

with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())

# import glob

# file_list = glob.glob('textFolder/trainingText/*.txt')
# file_list.sort()

# for textFile in file_list:
#     with open(textFile) as f:
#         text = f.readlines()
    
    # with open('test/{}.txt'.format((textFile.split('/')[1]).split(".")[0]), mode = 'w') as f:
    #     for s in text:
    #         if ('：' in s) and (not('＠' in s)):
    #             f.write("".join(s.split('：')[1:]))
    # with open('test/{}.txt'.format((textFile.split('/')[1]).split(".")[0])) as f:
    #     print(f.read())
