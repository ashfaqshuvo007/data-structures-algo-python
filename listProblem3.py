# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

userInput = int(input("Enter a number: "))
oddNumbers = []
for i in range(userInput):
    if i % 2 == 1:
        oddNumbers.append(i)
print(oddNumbers)