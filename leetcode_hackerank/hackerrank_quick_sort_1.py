#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(lst):
    if len(lst) <= 1:
        return lst

    basic_element = lst.pop()
    lst_left = []
    lst_right = []

    for element in lst:
        if element >= basic_element:
            lst_right.append(element)
        else:
            lst_left.append(element)

    return quickSort(lst_left) + [basic_element] + quickSort(lst_right)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()