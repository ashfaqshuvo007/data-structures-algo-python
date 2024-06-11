
from functools import reduce
from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    productMap = []
    for i, num in enumerate(nums):
        newList = nums[:i] + nums[i+1:]
        productMap.append(reduce(lambda x, y: x * y, newList, 1))
    return productMap

if __name__ == '__main__':
    # nums = [1,2,3,4]
    nums = [0,0]
    print(productExceptSelf(nums))