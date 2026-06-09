
#* 3689. Maximum Total Subarray Value I
"""
You are given an integer array nums of length n and an integer k.

You need to choose exactly k non-empty subarrays nums[l..r] of nums. 
Subarrays may overlap, and the exact same subarray (same l and r) 
can be chosen more than once.

The value of a subarray nums[l..r] is defined as: max(nums[l..r]) - min(nums[l..r]).

The total value is the sum of the values of all chosen subarrays.

Return the maximum possible total value you can achieve.

#? Example 1:

Input: nums = [1,3,2], k = 2

Output: 4

Explanation:

One optimal approach is:

Choose nums[0..1] = [1, 3]. The maximum is 3 and the minimum is 1, giving a value of 3 - 1 = 2.
Choose nums[0..2] = [1, 3, 2]. The maximum is still 3 and the minimum is still 1, so the value is also 3 - 1 = 2.
Adding these gives 2 + 2 = 4.

#? Constraints:

1 <= n == nums.length <= 5 * 10​​​​​​^4
0 <= nums[i] <= 109
1 <= k <= 105

"""
from typing import List
class Solution:
    #? Explanation: For any subarray the Max cannot exceed the Global MAX. Also, min cannot be less than global MIN
    #? Hence, this solution | Time: O(n) | Space: O(1)
    
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        maxNum = max(nums)
        minNum = min(nums)

        return (maxNum - minNum) * k