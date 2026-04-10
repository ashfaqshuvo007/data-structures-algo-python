nums = [0,0,1,1,1,2,2,3,3,4]

left = 1

for right in range(1, len(nums)):
    if nums[right] != nums[right-1]:
        nums[left] = nums[right]
        left += 1

# In the problem description, it is mentioned that the first k elements of the array should hold the final result.
#  So, we can simply return left as the length of the array with unique elements.
print(nums)
# print(left)