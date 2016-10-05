import sys
import os

file_name = sys.argv[1]
if not os.access(file_name, os.R_OK) or not file_name:
    print "File does not exist"
    exit()


print os.path.getsize(file_name)
