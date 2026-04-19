
s = "AABABBA"
k = 1


count = {}
res = 0

l = 0
maxFreq = 0
for r in range(len(s)):
    count[s[r]] = 1 + count.get(s[r], 0)
    maxFreq = max(maxFreq, count[s[r]])
    # if (r - l + 1) - max(count.values()) > k:
    if (r - l + 1) - maxFreq > k:
        count[s[l]] -= 1
        l += 1
    
    res = max(res, (r - l + 1))

print(res)
    