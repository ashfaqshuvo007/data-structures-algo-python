
#* 2161. Partition Array According to Given Pivot - MEDIUM

"""
You are given a 0-indexed integer array nums and an integer pivot. 
Rearrange nums such that the following conditions are satisfied:

Every element less than pivot appears before every element greater than pivot.
Every element equal to pivot appears in between the elements less than and greater than pivot.
The relative order of the elements less than pivot and the elements greater than pivot is maintained.

More formally, consider every pi, pj where pi is the new position 
of the ith element and pj is the new position of the jth element. 
If i < j and both elements are smaller (or larger) than pivot, then pi < pj.

Return nums after the rearrangement.

#? Example 1:

Input: nums = [9,12,5,10,14,3,10], pivot = 10
Output: [9,5,3,10,10,12,14]
Explanation: 
The elements 9, 5, and 3 are less than the pivot so they are on the left side of the array.
The elements 12 and 14 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [9, 5, 3] and [12, 14] are the respective orderings.

#? Example 2:

Input: nums = [-3,4,3,2], pivot = 2
Output: [-3,2,4,3]
Explanation: 
The element -3 is less than the pivot so it is on the left side of the array.
The elements 4 and 3 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [-3] and [4, 3] are the respective orderings.

"""


from typing import List
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        #Approach 1: Naive Iteration with Extra memory for three arrays
        # Time: O(n) | Space: O(l + r + p), l=left, r=right, p= pivot
        # leftArray = []
        # rightArray = []
        # pivotArray = []

        # for num in nums:
        #     if num < pivot:
        #         leftArray.append(num)
        #     elif num > pivot:
        #         rightArray.append(num)
        #     else:
        #         pivotArray.append(num)
        
        # return leftArray + pivotArray + rightArray

        #Approach 2: Iteration with InPlce with extra memory
        # Time: O(n) | Space: O(n)

        result = [0] * len(nums)
        i, j = 0, len(nums) - 1
        i2, j2 = 0, len(nums) - 1

        while i < len(nums):
            if nums[i] < pivot:
                result[i2] = nums[i]
                i2 += 1
            if nums[j] > pivot:
                result[j2] = nums[j]
                j2 -= 1
            i, j = i + 1, j - 1
        
        while i2 <= j2:
            result[i2] = result[j2] = pivot
            i2, j2 = i2 + 1, j2 - 1
            
        return result