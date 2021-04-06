################
# Problem One  #
###############

# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
#   i.  What was the average temperature in first week of Jan
#   ii. What was the maximum temperature in first 10 days of Jan
# Figure out data structure that is best for this problem

import csv
import os




if __name__ == '__main__':
    arr = []
    cwd = os.getcwd()

    with open(cwd + "/nyc_weather.csv", "r") as file:
        #skips the header
        next(file) 
        for row in file:
            tokens = row.split(',')
            date = tokens[0]
            temp = int(tokens[1])
            arr.append(temp)
    print(arr)

    # average_temp(arr)
    average_seven_temp = sum(arr[0:7]) / len(arr[0:7])
    print("Average temp of first 7 days: ", average_seven_temp)

    #MAximum temp
    max_temp = max(arr[0:10])
    print("Maxx temp: ",max_temp)

