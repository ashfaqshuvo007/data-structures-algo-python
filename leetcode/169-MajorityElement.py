nums = [2, 2, 1, 1, 1, 2, 2]    

from collections import defaultdict


count = defaultdict(int)
res = maxCount = 0

for num in nums:
    count[num] += 1

    if count[num] > maxCount:
        res = num
        maxCount = count[num]

print(res)   