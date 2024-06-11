"""
Given an array of strings 'strs', group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

"""
from collections import defaultdict


def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for word in strs:
        sortedWord = ''.join(sorted(word))
        if  sortedWord not in anagrams:
            anagrams[sortedWord] = [word]
        else: 
            anagrams[sortedWord].append(word)
    print(list(anagrams.values()))
            
if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    groupAnagrams(strs)