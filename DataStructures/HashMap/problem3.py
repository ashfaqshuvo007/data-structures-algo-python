################
# Problem Three#
###############

# npoem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python and print every word and its count as show below. Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.

import os


if __name__ == '__main__':
    word_count = {}
    cwd = os.getcwd()

    with open(cwd + "/poem.txt", "r") as file:
        for line in file:
            tokens = line.split(' ')
            for token in tokens:
                token.replace('\n', '')
                if token in word_count:
                    word_count[token] += 1
                else:
                    word_count[token] = 1
    
    print(word_count)

