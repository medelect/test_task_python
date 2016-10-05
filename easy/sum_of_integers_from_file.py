import os
import sys

sum_numb = 0
with open(sys.argv[1], 'r') as data:
    for num in data:
        sum_numb += int(num)

print sum_numb
