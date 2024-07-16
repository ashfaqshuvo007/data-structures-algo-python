'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

*** NEED TO REVISIT ***
'''

def trap(self, height: List[int]) -> int:
    if not height:
        return 0
    
    l, r = 0, len(height) - 1
    ml, mr = height[l], height[r]
    res = 0

    while l < r:
        if ml < mr:
            l += 1
            ml = max(ml, height[l])
            res += (ml - height[l])
        else:
            r -= 1
            mr = max(mr, height[r])
            res += (mr - height[r])
    return res
        