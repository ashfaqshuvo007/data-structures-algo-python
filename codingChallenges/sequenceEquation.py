# Given a sequence of  integers,  where each element is distinct and satisfies . For each  where , that is  increments from  to , find any integer  such that  and keep a history of the values of  in a return array.

# Example


# Each value of  between  and , the length of the sequence, is analyzed as follows:

# , so 
# , so 
# , so 
# , so 
# , so 
# The values for  are .

# Function Description

# Complete the permutationEquation function in the editor below.

# permutationEquation has the following parameter(s):

# int p[n]: an array of integers
# Returns

# int[n]: the values of  for all  in the arithmetic sequence  to 
# Input Format

# The first line contains an integer , the number of elements in the sequence.
# The second line contains  space-separated integers  where
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter

def permutationEquation(p):
    result = [0] * (len(p) + 1) 
    temp = [0]
    for i in p:
        temp.append(i)
    p = temp
    
    for i in range(1,len(p)):
        result[p[p[i]]] = i
    
            
    return result[1:len(p)]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
