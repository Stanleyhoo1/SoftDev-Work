# UWSD 21
# UWSD
# SoftDev
# K06 -- The More You Know About Your Data
# 2024-9-19
# time spent: 0.5

'''
DISCO:
...
QCC:
...
HOW THIS SCRIPT WORKS:
...
'''

import csv
import random

def read_csv(csvfile):
    with open(csvfile, newline='') as csv_file:
        header = next(csv_file)
        percent = 0.0
        content = csv.reader(csv_file)
        dic = {}
        for row in content:
            percent += float(row[1])
            percent = round(percent, 1)
            dic[percent] = row[0]

        dic.popitem()
        return dic
    
def choose_random(csvfile):
    data = read_csv(csvfile)
    keys = [key for key in data.keys()]
    random_num = random.random() * 99.8
    for i in range(len(keys)):
        if keys[i] > random_num:
            return data[keys[i-1]]
    
print(choose_random('occupations.csv'))