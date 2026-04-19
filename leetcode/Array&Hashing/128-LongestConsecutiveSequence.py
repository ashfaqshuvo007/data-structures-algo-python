'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

'''
# 4305ms 31.77mb O(n)
def longestConsecutive(self, nums: List[int]) -> int:
    numSet = set(nums)
    longest = 0

    for n in nums:
        # Check if it is the start of the sequence
        if (n - 1) not in numSet:
            length = 1
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
            
    return longest

## 339ms 31.81mb O(n) Just changed looping through the nums list to numSet directly

def longestConsecutive2(self, nums: List[int]) -> int:
    numSet = set(nums)
    longest = 0
    
    for n in numSet:
        if (n - 1) not in numSet:
            length = 1
            while (n + length) in numSet:
                length += 1

            longest = max(length, longest)
    return longest