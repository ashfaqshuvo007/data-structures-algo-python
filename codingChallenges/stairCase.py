# Staircase detail

# This is a staircase of size :

#    #
#   ##
#  ###
# ####
# Its base and height are both equal to . It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

# Write a program that prints a staircase of size .

# Function Description

# Complete the staircase function in the editor below.

# staircase has the following parameter(s):

# int n: an integer
# Print

# Print a staircase as described above.
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for i in range(1,n + 1):
        space = " "
        character = "#"
        output = str((n-i) * space) + str(character * i)
        print(output)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
