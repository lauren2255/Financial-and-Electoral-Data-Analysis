#import modules to run functions
import os
import csv

#path to collect budget data from Resources folder
budgetdata_csv = os.path.join('..', 'Resources', 'budget_data.csv')

#define function
def analysis (budgetdata):
    date = str(budgetdata[0])
    amount = int(budgetdata[1])

    months = []
    amt_total = []
    avg_change = []
    
    for rows in budgetdata:
        months.append(date[:3])
        amt_total.append(budgetdata[1])

    # change = 
    # avg_change = average(change)


    # for i in budgetdata:
    #     if inc_amount == max(inc_amount) in amount:
    #         inc_date = 
    
    #     if dec_amount == max(dec_amount) in amount:
    #         dec_date = 
    
# Read in the CSV file
with open(budgetdata_csv, 'r') as csvfile:

    # Split the data based on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    print(f'Financial Analysis')
    print(f' --------------------')
    print(f'Total Months: {months}')
    print(f'Total: {total}')
    print(f'Average Change:{avg_change}')
    print(f'Greatest Increase in Profits: {inc_date} ({inc_amount})')
    print(f'Greatest Decrease in Profits: {dec_date} ({dec_amount})')
