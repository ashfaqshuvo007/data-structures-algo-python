
#* 215. Kth Largest Element in an Array - MEDIUM

'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

#? Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

#? Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

#? Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104 # IMPORTANT
'''
from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # APROACH 1: MaxHeap | Time: O(n log k) | Space: O(n)
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)

        res = []

        while k > 0:
            num = -heapq.heappop(maxHeap)
            res.append(num)
            k -= 1

        return res[-1]

        # Aproach 2: MinHeap of length K | Time: O(n log k) | Space: O(k)

        # minHeap = []
        # for n in nums:
        #     heapq.heappush(minHeap, n)

        #     if len(minHeap) > k:
        #         heapq.heappop(minHeap)
        # return minHeap[0]

        # Aproach 3: MinHeap of length K but with heapq functiions| Time: O(n log k) | Space: O(k)
        # return heapq.nlargest(k, nums)[-1]