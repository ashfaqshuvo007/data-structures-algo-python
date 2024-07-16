'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

'''

def maxArea(self, height: List[int]) -> int:
    l, r = 0, len(height) - 1
    maxArea = 0

    while(l < r):
        area = (r - l) * min(height[l], height[r])
        
        if height[l] < height[r]:
            l += 1
        elif height[r] < height[l]:
            r -= 1
        else:
            #Does not matter which one we shift
            # Another way is to shift the one which has a larger height coming up
            # We are shift left pointer
            l += 1
        maxArea = max(maxArea, area)
    
    return maxArea