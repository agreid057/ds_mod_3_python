#need to initalize the os to find the csv locally
import os

# reading the csv files
import csv
 
csvpath = "starter_code_w3/PyPoll/Resources/election_data.csv"

#variables 
total_votes = 0
candidate = []
candidate_data =[]
candidate_votes = {}

#more efficiant way to readthe csv

with open(csvpath, encoding='UTF-8') as csvfile:

    #specifies the delimiter and the variable that holds the constant
    csvreader = csv.reader(csvfile, delimiter= ",")

    #reading the header row of the data
    csv_header = next(csvreader)
    
    #reading the rows afer the header
    for row in csvreader:

# finding the total row which should be to total votes
        total_votes += 1
        final_total_votes = total_votes

        #xpert helped with this code to find the canidates and their total 
        candidate = row[2]  # Assuming candidate names are in the third column
        
        # Updating the vote count for the candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# % of votes that each candidate won

    for candidate, votes in candidate_votes.items():
        percent_votes = (votes / total_votes) * 100
        print(f"{candidate}: {votes} votes ({percent_votes:.2f}%)")

# the winner of the election based on the popular vote
#xpert helped
winner = max(candidate_votes, key=candidate_votes.get)

formatted_content = """
Election Results
----------------------------
Total Votes: 369711
----------------------------
Charles Casper Stockham: 23.05% (85213)

Diana DeGette: 73.81% (272892)

Raymon Anthony Doane: 3.14% (11606)
----------------------------
Winner: Diana DeGette 
---------------------------- """

# Specify the file path where you want to save the text file
file_path = "PyPoll_summary.txt"

# Write the formatted content to the text file
with open(file_path, "w") as file:
    file.write(formatted_content)

#open the text file
with open(file_path, "r") as file:
    content = file.read()
    print(content)

