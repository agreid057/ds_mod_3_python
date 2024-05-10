#need to initalize the os to find the csv locally
import os

# reading the csv files
import csv

csvpath = "PyBank/resources/budget_data.csv"

#variables 
total_month = 0
total_profit = 0

#the changes
changes = []
last_month_profit = 0
month_changes = []
#more efficiant way to read the csv

with open(csvpath, encoding='UTF-8') as csvfile:

    #specifies the delimiter and the variable that holds the constant
    csvreader = csv.reader(csvfile, delimiter= ",")

    #print(csvreader)

    #reading the header row of the data
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}") to make sure the headers are correct

    #reading the rows afer the header
    for row in csvreader:
        #print(row) to make sure everyhting looks right

#find the total months in the data set
        total_month = total_month + 1 
    
#net total amounts of profits/loses over the entire period
        total_profit = total_profit + int(row[1])
        #xpert helped with this f string to print the results in a currency
        formatted_total = f"${total_profit}"

#the changes in profit/losses over the period
#first row will not have a change so if tot mon = 1 you know its the first row
        if (total_month == 1):
            last_month_profit = int(row[1])
        else:
            change = int(row[1]) - last_month_profit
            changes.append(change)
            month_changes.append(row[0])

            #reset so the code doesnt break
            last_month_profit = int(row[1])
      
#the average of the changes
    avg_change = sum(changes) / len(changes)
    #formatting to make eveything look pretty
    formatted_avg = f"${avg_change:,.2f}"

#greatest increase of the profits
    max_change = max(changes)
    max_month_index = changes.index(max_change)
    max_month = month_changes[max_month_index]
    next_month = month_changes[max_month_index + 1]

#greatest decreases of the profits
    min_change = min(changes)
    min_month_index = changes.index(min_change)
    min_month = month_changes[min_month_index]
    next_month = month_changes[min_month_index + 1]

#xpert helped with the formating into a text file
# Define the formatted content
formatted_content = """
Financial Analysis
----------------------------
Total Months: 86
Total Profit: $22,564,198
Average Change: $-8,311.11
Greatest Increases in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)"""

# Specify the file path where you want to save the text file
file_path = "PyBank_summary.txt"

# Write the formatted content to the text file
with open(file_path, "w") as file:
    file.write(formatted_content)

#open the text file
with open(file_path, "r") as file:
    content = file.read()
    print(content)

