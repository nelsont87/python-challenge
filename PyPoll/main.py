import os
import csv

csvpath = os.path.join("election_data.csv")

totalVotes = 0
candidate = []
candVote = {}


# opening csv file to read
with open(csvpath, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # iterating through csv to append elements to new lists
    for row in csvreader:
        totalVotes += 1
        # Add candidate to list and dictionary
        if row[2] not in candidate:
            candidate.append(row[2])
            candVote.update({row[2]: 0})
        # Count candidate votes
        if row[2] in candVote:
            candVote[row[2]] += 1

# making a copy of canditate votes to get percent
candPerc = dict()
candPerc.update(candVote)
# update key values to be percentages
for key in candPerc:
    candPerc[key] = float(candPerc[key] / totalVotes)

# Getting winner of vote
win = max(candVote, key = candVote.get)

# print answer
f = open("output.txt", "a")


print("Election Results", file=f)
print("Election Results")
print("-----------------------------", file=f)
print("-----------------------------")
z =  "Total Votes: %s" % (totalVotes)
print(z, file=f)
print(z)
print("-----------------------------", file=f)
print("-----------------------------")

for key in candPerc:
    print(key + ": " + "{:.2%}".format(candPerc[key]) + " (" + str(candVote[key]) + ")", file=f)
for key in candPerc:
    print(key + ": " + "{:.2%}".format(candPerc[key]) + " (" + str(candVote[key]) + ")")

print("-----------------------------", file=f)
print("-----------------------------")

y = "Winner: %s" % (win)
print(y, file=f)
print(y)

print("-----------------------------", file=f)
print("-----------------------------")


f.close()

# #print(win)
# #print(totalVotes)
# #print(candidate)
# #print(candVote)
# #print(candPerc)