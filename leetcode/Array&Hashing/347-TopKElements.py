"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

"""
from collections import Counter
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    # Using counter 
    elementsMap = Counter(nums)
    # sorted in descending order
    sortedMap = sorted(elementsMap.items(), key=lambda item: item[1], reverse=True)
    # return top k elements as a list
    return [item[0] for item in sortedMap[:k]]

if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2
    print(topKFrequent(nums, k))