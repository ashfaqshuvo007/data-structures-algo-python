#* Beautiful Explanation:
#===============================
# Notes: (Please Correct If you feel it doesnt work):
# Funda 1: There is one messy half and one one sorted half
# Funda 2: Calculate mid = left + (right-left)//2
# Funda 3: If number to find is known, you can check for it in sorted half, and if not found, discard sorted half and repeat the process in unsorted half
# Funda 4: If the number to find is unknown like find minimum, always check in unsorted half
# Funda 5: Always compare mid to right to find which side is sorted half and which side is unsorted half
# 5.1 : If arr[mid] > arr[right] -> mid->right is unsorted and left->mid is sorted
# 5.2 : If arr[mid] < arr[right] -> mid->right is sorted, left->mid is unsorted
# Funda 6: If your answer lies 100% within the array, then use left < right to trap the answer, meaning leave precisely one element before exiting the loop
# Funda 7: If your answer lies maybe or may not be in array, then use left <= right condition and let pointers cross to exit
# Funda 8: When moving the pointers, if you are on unsorted end (mid>right), always move the left pointer to mid + 1 because anything on the left is sorted and has to be bigger than right, including the mid itself which we just tested
# Funda 9: If you are on sorted end (mid<right), move the right pointer to mid, because mid can be the starting point or inflection point or part of fully sorted array

from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) //2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        
        return nums[l]

if __name__ == "__main__":
    solution = Solution()
    nums = [3,4,5,1,2]
    result = solution.findMin(nums)
    print(result)
    