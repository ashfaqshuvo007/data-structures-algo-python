
#* Recusion Basic examples:

#? Recursively calculate the sum of list of numbers
from typing import List
class Recursion:
    def recursive_sum(self, nums: List[int]) -> int: 
        if not nums:
            return 0
        return nums[0] + self.recursive_sum(nums[1:])

    def count_items(self, arr: List[any]) -> int:
        if not arr:
            return 0
        return 1 + self.count_items(arr[1:])

    def max_num(self, nums: List[int]) -> int:
        if not nums:
            return -1
        maxNum = nums[0]
        return max(maxNum, self.max_num(nums[1:]))

    def binary_search(self, nums: List[int], l: int, r: int, target: int) -> bool:
        m = (l + r) // 2

        if nums[m] == target:
            return True

        if  target < nums[m]:
            return self.binary_search(nums,l, m - 1, target)
        if target > nums[m]:
            return self.binary_search(nums,m + 1, r, target)


if __name__ == "__main__":
    numsList = [10, 20, 30, 40, 50, 60]
    recursion = Recursion()

    #* Recursively calculate the sum of array elements
    # sum_recursive = recursion.recursive_sum(numsList)
    # print(sum_recursive)

    #* Recursively calculate the number of elements in an array
    # mixedList = [10, 20, "30", 40, "50", 60]
    # count_items = recursion.count_items(mixedList)
    # print(count_items)

    #* Recursively calculate the max of array elements
    # max_num = recursion.max_num(numsList)
    # print(max_num)

    #* Recursive Binary Search
    print(recursion.binary_search(numsList,0, len(numsList) -1, 60))