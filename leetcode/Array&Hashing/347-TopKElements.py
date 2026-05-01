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
    #* Approach1: Using counter in-built function.
    # elementsMap = Counter(nums)
    # # sorted in descending order
    # sortedMap = sorted(elementsMap.items(), key=lambda item: item[1], reverse=True)
    # # return top k elements as a list
    # return [item[0] for item in sortedMap[:k]]

    #* Approach 2: Using Bucket Sort
    # Frequency Map
    count = {}
    # Bucket: indices are counts and values are list of nums with that count
    bucket = [[] for _ in range(len(nums) + 1)]

    # Create the freq map
    for num in nums:
        count[num] = 1 + count.get(num, 0)
    
    #Create the bucket
    for n, c in count.items():
        bucket[c].append(n)
    
    #Finally iterate the bucket in reverse
    # get the top k frequent elements
    res = []

    for i in range(len(bucket) - 1, 0, -1):
        for n in bucket[i]:
            res.append(n)
            if len(res) == k:
                return res
    

    #TODO: Approach 3: Using Min Heap


if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2
    print(topKFrequent(nums, k))