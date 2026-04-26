from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Approach 1: Using hash set to track visited numbers.
        # visited = set()
        # for i in range(len(nums)):
        #     if nums[i] in visited:
        #         return nums[i]
        #     else:
        #         visited.add(nums[i])

        #Approach 2: Marking the visited numbers by negating the val. O(n) time and o(1) space.
        # for num in nums:
        #     idx = abs(num) - 1
        #     if nums[idx] < 0:
        #         return abs(num)
        #     nums[idx] *= -1
        # return -1

        # Approach 3: Floyd's Algo - O(n) time and no extra space.
        slow, fast = 0 , 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        
    
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3, 4, 2, 2]
    result = solution.findDuplicate(nums)
    print(result)
    