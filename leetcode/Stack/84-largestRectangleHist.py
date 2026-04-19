from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #? Intuition
        # We want, for each bar, the widest area where it can act as the shortest bar.
        # With a single pass and a stack, we can do this on the fly:

        # We keep a stack of bars in increasing height order, each stored with the earliest index where that height can start.
        # When we see a new bar that is shorter than the top of the stack, it means the taller bar on top can’t extend further to the right.
        # So we pop it and compute the area it could cover.
        # The new shorter bar can start from as far left as the popped bar’s start index, so we reuse that index.
        # After the pass, we compute areas for any bars still in the stack, extending them to the end.
        # Each bar is pushed and popped at most once, giving an efficient, one-pass solution.
        
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                maxArea = max(maxArea, (height * (i- idx)))
                start = idx

            stack.append((start, h))
        
        for i, h in stack:
            maxArea = max(maxArea, (h * (len(heights) - i)))
        
        return maxArea
    
if __name__ == "__main__":
    solution = Solution()
    heights = [2,1,5,6,2,3]
    result = solution.largestRectangleArea(heights)
    print(result)

