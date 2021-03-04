#!python3
import glob, random

file_list = glob.glob('../textFolder/allTextFolder/*.txt')
rand = random.sample(file_list, int((len(file_list)*0.7)))

for path in rand:
    print(path)