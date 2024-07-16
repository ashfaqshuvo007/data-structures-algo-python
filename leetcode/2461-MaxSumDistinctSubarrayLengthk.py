'''
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

- The length of the subarray is k, and
- All the elements of the subarray are distinct.
- Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.
'''
def maximumSubarraySum(self, nums: List[int], k: int) -> int:
    
    # Initialize a counter for the first 'k' elements
    counter = Counter(nums[:k])

    # Calculate the sum of the first 'k' elements
    cSum = sum(nums[:k])

    # If the number of unique elements equals 'k', assign cSum to 'mSum', else 0
    mSum = cSum if len(counter) == k else 0
    
    for i in range(k, len(nums)):
        # Increase the count of ith element in counter
        counter[nums[i]] += 1
        cSum += nums[i]

        # decrease the count of the element outside window
        counter[nums[i - k]] -= 1
        cSum -= nums[i - k] # subtract the number from the cSum

        # if there are mo (i - k)th element in counter
        if counter[nums[i - k]] == 0:
            del counter[nums[i - k]]
        
        if len(counter) == k:
            mSum = max(mSum, cSum)

    return mSum