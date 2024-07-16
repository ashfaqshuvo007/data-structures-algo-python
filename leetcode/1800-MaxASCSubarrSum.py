'''
Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending.
'''
def maxAscendingSum(self, nums: List[int]) -> int:
    cSum, mSum, prev = 0, -999999, -999999
    cSubArray = []
    for i in range(0, len(nums)):
        if nums[i] > prev:
            cSum += nums[i]
        else:
            cSum = nums[i]
        mSum = max(mSum, cSum)
        prev = nums[i]
    
    return mSum