# Stanley Hoo
# UWSD
# SoftDev
# K04 -- Python dictionaries and random seleciton
# 2024-9-13
#time spent:

import random

def make_dict(filename):
    file = open(filename, 'r')
    contents = file.read()
    file.close()
    all_content = contents.split('@@@')
    dic = {}
    index = 0
    for i in all_content:
        info = i.split('$$$')
        dic[index] = (info[0], info[1], info[2])
        index += 1
    return dic
    
def choose_random(filename):
    dic = make_dict(filename)
    info = dic[int(random.random()*len(dic))]
    return f'Name: {info[1]}, Period: {info[0]}, Ducky: {info[2]}'
    
print(choose_random('krewes.txt'))