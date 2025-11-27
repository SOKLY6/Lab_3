#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(lst):
    if not lst:
        return []
    
    max_element = max(lst)
    min_element = min(lst)
    result_list = []

    if min_element >= 0:
        counting_list = [0 for i in range(max_element + 1)]

        for element in lst:
            counting_list[element] += 1

        for i in range(max_element + 1):
            result_list += [i] * counting_list[i]

    else:
        counting_list = [0 for i in range(max_element - min_element + 1)]

        for element in lst:
            counting_list[element + abs(min_element)] += 1

        for i in range(max_element - min_element + 1):
            result_list += [i + min_element] * counting_list[i]
    
    return result_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()