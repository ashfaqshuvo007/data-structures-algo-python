#python lists. It is a mutable data structure i.e. items can be added to it after creation
# It is a dynamic array behind the scenes

##############
# PROBLEM    #
##############
#Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190

#Create a list to store these monthly expenses and using that find out,




#array
monthlyExpenses = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
diff = monthlyExpenses[1] - monthlyExpenses[0]
print(diff)
# 2. Find out your total expense in first quarter(first three months) of the year.
fistQuarterExpense = monthlyExpenses[0]+monthlyExpenses[1]+monthlyExpenses[2]
print(fistQuarterExpense)

# 3. Find out if you spent exactly 2000 dollars in any month
print('Did I spend 2000 in any month? ', 2000 in monthlyExpenses)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
monthlyExpenses.append(1980)
print("After june expense: ", monthlyExpenses)

# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this

monthlyExpenses[3] = monthlyExpenses[3] - 200

print("Expenses after return in april: ", monthlyExpenses)