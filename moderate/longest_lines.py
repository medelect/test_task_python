import os
import sys


file_name = sys.argv[1] 
if not os.access(file_name, os.R_OK):
    print "File does not exist"
    exit()

string_list = []
with open(file_name, 'r') as data:
    for string in data:
        string_list.append(string[:-1])

counter = int(string_list.pop(0))
string_list.sort(key=len,reverse=True)

for item in string_list[0:counter]:
    print item
