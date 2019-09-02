import os
import csv

csvpath = os.path.join("employee_data.csv")

empName = []
empFirst = []
empLast = []

# opening csv file to read
with open(csvpath, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        empName.append(row[1])


for name in empName:
    empFirst.append(name.split()[0])

for name in empName:
    empLast.append(name.split()[1])


print(empFirst)
print(empLast)
