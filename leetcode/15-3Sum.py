'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''
def threeSum(self, nums: List[int]) -> List[List[int]]:
    if all(i == 0 for i in nums): #Handle edge cases
        return [ [0] * 3]
    nums.sort() 
    resultList = set()

    for i, a in enumerate(nums):
        if a == 0 and a == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            threeSum = a + nums[left] + nums[right] # 1st: 0, 0 , 0

            if threeSum > 0:
                right -= 1
            elif threeSum < 0:
                left += 1
            else:
                resultList.add((a, nums[left], nums[right]))
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    return [list(triplet) for triplet in resultList]
