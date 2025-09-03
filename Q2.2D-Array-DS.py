# Given a 6 X 6 2D array, arr , an hourglass is a subset of values with indices falling in the following pattern:
# There are 16 hourglasses in a 6 X 6  array. The hourglass sum  is the sum of the values in an hourglass. Calculate the hourglass sum for every hourglass in , then print the  hourglass sum.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    maxsum=-99
    for i in range(4):
        for j in range(4):
            #top
            top=sum(arr[i][j:j+3])

            #mid
            mid=arr[i+1][j+1]

            #bottom
            bottom=sum(arr[i+2][j+3])

            hourglass=top + mid +bottom

            maxsum=max(hourglass,maxsum)
    return maxsum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
