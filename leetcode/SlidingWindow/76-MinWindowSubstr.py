class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #Base case
        if t == "":
            return ""
        
        # Step 1: frequency map for t
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # e.g. {A: 1, B:1, C:1}
        
        #Step 2: Initializing variables for the algo
        window = {} # Counter Map for current window

        # For cheking validity of current window
        have = 0
        need = len(countT)

        # For results
        res = [-1, -1] # (left, right) Smallest valid window
        resLen = float("infinity") # Result length for handling edgecase

        # Step 3: Traverse 's' string to find solution with two pointers
        left = 0
        for right in range(len(s)):
            c = s[right] 
            window[c] = 1 + window.get(c, 0) #increment c count in current window
            
            # if current c is in countT and it is also present in t, we have what one that we need
            if c in countT and window[c] == countT[c]:
                have += 1
            
            # while we found valid substring of t
            while have == need:
                # Update results if current window is smaller
                currentWindow = right - left + 1
                if currentWindow < resLen:
                    res = [left, right]
                    resLen = currentWindow
                # Shrink the window from left 
                window[s[left]] -= 1

                # With new size if char at s[l] 
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        
        # Step 4: Return results till current right (+1 coz indices)if resLen != infinity otherwise, ""
        left, right = res
        return s[left : (right + 1)] if resLen != float("infinity") else ""
    

if __name__ == "__main__":
    solution = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    result = solution.minWindow(s, t)
    print(result)
        