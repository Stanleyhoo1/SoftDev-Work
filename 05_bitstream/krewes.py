# Stanley Hoo
# 
# SoftDev
# K04 -- Python dictionaries and random seleciton
# 2024-9-13
#time spent:

def make_dict(filename):
    file = open(filename, 'r')
    contents = file.read()
    file.close()
    all_content = contents.split('@@@')
    dic = {}
    for i in all_content:
        info = i.split('$$$')
        dic[info[1]] = (info[0], info[1], info[2])
    print(dic)
    
make_dict('krewes.txt')