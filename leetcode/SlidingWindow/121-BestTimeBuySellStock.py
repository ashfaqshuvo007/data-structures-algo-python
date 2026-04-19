prices = [7,1,5,3,6,4]
maxProfit = 0
left = 0
right = 1

while right < len(prices):
    if prices[left] < prices[right]:
        maxProfit = max(maxProfit, (prices[right] - prices[left]))
    else:
        left = right
    right += 1
    
print(maxProfit)

# ======== Brute Force =========
# ACCEPTED - O(n*2)/ O(1)
# maxProfit = 0
#for i in range(len(prices)):
#    for j in range(i + 1, len(prices)):
#        maxProfit = max(maxProfit, (prices[j] - prices[i]))
#print(maxProfit)
