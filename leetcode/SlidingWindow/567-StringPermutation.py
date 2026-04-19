s1 = "ab"
s2 = "eidbaooo" 
        
if len(s1) > len(s2) : print(False)

# Freq arrays
s1Count, s2Count = [0] * 26, [0] * 26

for i in range(len(s1)):
    s1Count[ord(s1[i]) - ord('a')] += 1
    s2Count[ord(s2[i]) - ord('a')] += 1

# Matches will act as the measure of how the two strings match
matches = 0
for i in range(26):
    matches += (1 if s1Count[i] == s2Count[i] else 0)

## SLIDING WINDOW
left = 0
for right in range(len(s1), len(s2)):
    if matches == 26:
        print(True)
        exit()
    
    #Coz, we are using arrays for count, mapping the char to index
    index = ord(s2[right]) - ord('a')
    s2Count[index] += 1
    if s1Count[index] == s2Count[index]:
        matches += 1
    elif s1Count[index] + 1 == s2Count[index]:
        matches -= 1

    index = ord(s2[left]) - ord('a')
    s2Count[index] -= 1
    if s1Count[index] == s2Count[index]:
        matches += 1
    elif s1Count[index] - 1 == s2Count[index]:
        matches -= 1
    left += 1

#Checking after loop exists
print(matches == 26)

# HASHMAp Solution - O(n * m ) / O(n) 
# WORKS BUT LONG TEST CASES FAIL
# count1 = {}
# for c in s1:
#     count1[c] = 1 + count1.get(c, 0)

# need = len(count1)
# for i in range(len(s2)):
#     count2, curr = {}, 0
#     for j in range(i, len(s2)):

#         count2[s2[j]] = 1 + count2.get(s2[j], 0)

#         # if curr char count exceeds that count1, break, no permutations
#         if count1.get(s2[j], 0) < count2[s2[j]]:
#             break

#         # if curr char count matched that in count1, increase curr for the character & we continue
#         if count1.get(s2[j], 0) == count2[s2[j]]:
#             curr += 1

#         # if curr count is equal to need length, we found
#         if curr == need:
#             return True

# # No permutations found
# return False