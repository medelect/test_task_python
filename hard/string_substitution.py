import os
import sys


file_name = sys.argv[1] 
if not os.access(file_name, os.R_OK):
    #print "File not exist"
    exit()

def convert(source):
    task_list = []
    with open(source, 'r') as data_in:
        for string in data_in:
            head = string[:-1].split(';')
            tail = head[1].split(',') 
            task_list.append([head[0],tail])
    return task_list

def handling(source):
    result = source[0]
    obj = source[0]
    pos = 0
    if len(source[1]) > 1:
        fr = source[1].pop(0)
        to = source[1].pop(0)
    elif len(source[1]) == 1:
        print 'incorrect number of arguments'
        exit()
    else:
        return result
    pos = obj.find(fr)
    obj = obj.replace(fr,'@',1)
    tmp = obj.split('@')
    obj = ''.join(tmp)
    obj = handling([obj, source[1]])
    tmp = [i for i in obj]
    tmp.insert(pos,to)
    obj = ''.join(tmp)
    return obj

for i in convert(file_name):
    print handling(i)

