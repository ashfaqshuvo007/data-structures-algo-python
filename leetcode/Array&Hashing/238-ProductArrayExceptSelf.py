
from functools import reduce
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #* Approach 1:
        #? With built in functions: O(n**2)
        # productMap = []
        # for i, num in enumerate(nums):
        #     newList = nums[:i] + nums[i+1:]
        #     productMap.append(reduce(lambda x, y: x * y, newList, 1))
        # return productMap

        #* Approach 2: 
        #? Using Suffix and Prefix: Time - O(n) Space - O(n)
        # n = len(nums)
        # pref = [0] * n
        # suff = [0] * n
        # res = [0] * n

        # # handle edge case for left and rightmost place
        # pref[0] = suff[n - 1] = 1

        # #Prefix Products
        # for i in range(1, n):
        #     pref[i] = nums[i - 1] * pref[i - 1]
        
        # #Suffix Products
        # for i in range(n - 2, -1, -1):
        #     suff[i] = nums[i + 1] * suff[i + 1]
        
        # # Result
        # for i in range(n):
        #     res[i] = pref[i] * suff[i]
        
        # return res


        #* Approach 3: 
        #? Using Suffix and Prefix (Most Optimal): Time - O(n) Space - *O(1)*

        n = len(nums)
        # result array
        res = [1] * n

        # Prefix product
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        # postfix product
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res


if __name__ == '__main__':
    nums = [1,2,3,4]
    # nums = [0,0]
    solution = Solution()
    print(solution.productExceptSelf(nums))