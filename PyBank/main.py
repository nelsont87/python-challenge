import os
import csv

csvpath = os.path.join("budget_data.csv")

monthCount = 0
totalProfit = 0
profitList = []
dateList = []
# opening csv file to read
with open(csvpath, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # iterating through csv to append elements to new lists
    for row in csvreader:
        monthCount += 1
        totalProfit = totalProfit + int(row[1])
        profitList.append(row[1])
        dateList.append(row[0])

# creating list that has the difference in elements
change = [int(profitList[i+1]) - int(profitList[i]) for i in range(len(profitList) - 1)]

# removing the first element to match up with the index of the change list
dateList.pop(0)

# average change list
avgChange = sum(change) / len(change)
avgChange = round(avgChange, 2)
#avgChange = [int(change[j])/2 for j in range(len(change))]
#print(avgChange)

# Finding max and min
profitMin = min(change)
profitMax = max(change)
# Finding index of max and min
indexMin = change.index(min(change))
indexMax = change.index(max(change))

# Finding corresponding date of max and min change
dateMin = dateList[indexMin]
dateMax = dateList[indexMax]

# Print answer

f = open("output.txt", "a")


print("Financial Analysis", file=f)
print("Financial Analysis")
print("-----------------------------", file=f)
print("-----------------------------")
z =  "Total Months: %s" % (monthCount)
print(z, file=f)
print(z)
y = "Total: %s" % (totalProfit)
print(y, file=f)
print(y)
x = "Average Change %s" % (avgChange)
print(x, file=f)
print(x)
a = "Greatest Increase in Profits: %s (%s)" % (dateMax, profitMax)
print(a, file=f)
print(a)
b = "Greatest Decrease in Profits: %s (%s)" % (dateMin, profitMin)
print(b, file=f)
print(b)

f.close()
