#import modules to run functions
import os
import csv

#path to collect budget data from Resources folder
cvspath = os.path.join('Resources', 'election_data.csv')

#making empty lists so that  append function can be used to add to them
votes = []
ccs_votes = []
dd_votes = []
rad_votes = []

# Read in the CSV file using the path
with open(cvspath, 'r') as csvfile:

    # Split the data based on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip first row and start analyzing based on second row
    header = next(csvreader)

    #for loop going through each row in csv
    for row in csvreader:
        votes.append(row[0])

        #conditional - if index 2 says vote was for x politician, add that name to the list above
        if row[2] == "Charles Casper Stockham":
            ccs_votes.append(row[2])
        elif row[2] == "Diana DeGette":
            dd_votes.append(row[2])
        elif row[2] == "Raymon Anthony Doane":
            rad_votes.append(row[2])

#make percents by diving length of list of row of specific politician votes by length of list of row of total votes
dd_percent = (len(dd_votes) / len(votes)) * 100
ccs_percent = (len(ccs_votes) / len(votes)) * 100
rad_percent = (len(rad_votes) / len(votes)) * 100

#conditional for if each politician's percent is higher than the others, winner variable equals that politician's name
if dd_percent > ccs_percent and rad_percent:
        winner = "Diane DeGette"
elif ccs_percent > dd_percent and rad_percent:
        winner = "Charles Casper Stockham"
elif rad_percent > dd_percent and ccs_percent:
        winner = "Raymon Anthony Doane"

print(f'Election Results')
print(f'--------------------')
#total votes = length of list of total votes
print(f'Total Votes: {len(votes)}')
print(f'--------------------')
#round for percent, votes for each candidate = the length of the list of their votes
print(f'Charles Casper Stockham: {round(ccs_percent, 3)}% ({len(ccs_votes)})')
print(f'Diana DeGette: {round(dd_percent, 3)}% ({len(dd_votes)})')
print(f'Raymon Anthony Doane: {round(rad_percent, 3)}% ({len(rad_votes)})')
print(f'--------------------')
#print winner based on conditional based on percent above
print(f'Winner: {winner}')
print(f'--------------------')

#make path for text file to be saved to
output_path = os.path.join('analysis', 'Election_Results.txt')

#write text file below
with open(output_path, 'w') as textfile:
    textfile.write("Election Results")
    #use to make new row
    textfile.write("\n")
    textfile.write("--------------------")
    textfile.write("\n")
    textfile.write(f'Total Votes: {len(votes)}')
    textfile.write("\n")
    textfile.write(f'Charles Casper Stockham: {round(ccs_percent, 3)}% ({len(ccs_votes)})')
    textfile.write("\n")
    textfile.write(f'Diana DeGette: {round(dd_percent, 3)}% ({len(dd_votes)})')
    textfile.write("\n")
    textfile.write(f'Raymon Anthony Doane: {round(rad_percent, 3)}% ({len(rad_votes)})')
    textfile.write("\n")
    textfile.write("--------------------")
    textfile.write("\n")
    textfile.write(f'Winner: {winner}')
    textfile.write("\n")
    textfile.write("--------------------")

