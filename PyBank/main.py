#import modules to run functions
import os
import csv

#path to collect budget data from Resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')
print(csvpath)

#make empty lists so append function can be used to add to them
months = []
amt_total = []
total_change = []

# Read in the csv file from the path
with open(csvpath, 'r') as csvfile:

    # Split the data based on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #there is a header, skip first row and start analyzing based on second row
    header = next(csvreader)
        
    #for loop to add values to the months + amt_total lists going down each row
    for row in csvreader:
        months.append(row[0])
        amt_total.append(int(row[1]))

    #for loop to cycle through amount values and calculate each change between 2 values
    for i in range(len(amt_total) - 1):
        total_change.append(amt_total[i + 1] - amt_total[i])

#identify greatest increase and decrease in profit change using max and min
max_inc_amt = max(total_change)
max_dec_amt = min(total_change)

#pull index number of max and min profit value + 1 since change is in between month values
max_inc_month_index = total_change.index(max(total_change)) + 1
max_dec_month_index = total_change.index(min(total_change)) + 1

#print financial analysis results to terminal
print(f'Financial Analysis')
print(f' --------------------')
#total months is equivalent to the amount of month values using the len function
print(f'Total Months: {len(months)}')
#total amount of profit is sum of each profit value
print(f'Total: ${sum(amt_total)}')
#average of the total changes in between profit values
print(f'Average Change: ${round(sum(total_change)/len(total_change), 2)}')
#pull month at the index where the profit change amount is highest
print(f'Greatest Increase in Profits: {months[max_inc_month_index]} (${max_inc_amt})')
#pull month at the index where the profit change amount is lowest
print(f'Greatest Decrease in Profits: {months[max_dec_month_index]} (${max_dec_amt})')

#make path for text file to be saved in
output_path = os.path.join('analysis', 'Financial_Analysis.txt')

#using path, write the following strings 
with open(output_path, "w") as textfile:
    textfile.write("Financial Analysis")
    #jump to new row using \n
    textfile.write("\n")
    textfile.write("----------------------")
    textfile.write("\n")
    textfile.write(f'Total Months: {len(months)}')
    textfile.write("\n")
    textfile.write(f'Total: ${sum(amt_total)}')
    textfile.write("\n")
    textfile.write(f'Average Change: ${round(sum(total_change)/len(total_change), 2)}')
    textfile.write("\n")
    textfile.write(f'Greatest Increase in Profits: {months[max_inc_month_index]} (${max_inc_amt})')
    textfile.write("\n")
    textfile.write(f'Greatest Decrease in Profits: {months[max_dec_month_index]} (${max_dec_amt})')