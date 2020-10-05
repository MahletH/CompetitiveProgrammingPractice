#!/bin/python3

import os
import sys
import heapq
#
# Complete the cookies function below.
#
def cookies(k, A):
    #
    # Write your code here.
    #
    counter=0
    heapq.heapify(A)
    while A:
        cur_min=heapq.heappop(A)
        if cur_min>=k:
            return counter
        if A:
            next_min=heapq.heappop(A)
            heapq.heappush(A,cur_min+2*next_min)
            counter+=1
        else:
            return -1
    return -1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
