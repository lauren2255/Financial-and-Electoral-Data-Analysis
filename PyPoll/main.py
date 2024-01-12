#import modules to run functions
import os
import csv

#path to collect budget data from Resources folder
election_data_csv = os.path.join('..', 'Resources', 'election_data.csv')

#define function
def analysis (budgetdata):

    votes = []
    candidates = []
    
    for row in election_data_csv:
        votes.append(count(election_data_csv[0]))



    # Read in the CSV file
with open(election_data_csv, 'r') as csvfile:

    # Split the data based on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    print(f'Election Results')
    print(f' --------------------')
    print(f'Total Votes: {votes}')
    print(f' --------------------')

    print(f' --------------------')
    print(f'Winner: {winner}')
    print(f' --------------------')