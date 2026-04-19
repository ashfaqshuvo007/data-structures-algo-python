
s = "abcabcbb"

substringSet = set()
left = 0
maxLen = 0

for right in range(len(s)):
    while s[right] in substringSet:
        substringSet.remove(s[left])
        left += 1
    substringSet.add(s[right])
    maxLen = max(maxLen, right - left + 1)

print(maxLen) 