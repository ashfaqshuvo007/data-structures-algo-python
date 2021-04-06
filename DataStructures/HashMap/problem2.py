################
# Problem Two  #
###############

# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
#   i.  What was the temperature on Jan 9?
#   ii. What was the temperature on Jan 4?

# Figure out data structure that is best for this problem

import csv
import os




if __name__ == '__main__':
    days = {}
    cwd = os.getcwd()

    with open(cwd + "/nyc_weather.csv", "r") as file:
        #skips the header
        next(file) 
        for row in file:
            tokens = row.split(',')
            date = tokens[0]
            temp = int(tokens[1])
            days[date] = temp
    print(days)

    #Temp on Jan 9
    print("Temp on jan 9: ", days['Jan 9'])
    #Temp on Jan 4
    print("Temp on jan 4: ",days['Jan 9'])

