""" # Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)

import csv
 """
""" 
import csv
# Assign a variable for the file to load and the path
file_to_load = 'Resources/election_results.csv'
#Open the file in read mode
election_data = file_to_load.read #open(file_to_load, 'r')
#or
#with open(file_to_load, 'r') as election_data:
#to do Analysis
print(election_data)
#Close file
#election_data.close()
 """
""" import csv
import os

# Get the CURRENT directory that THIS file is inside of
cwd = os.getcwd()

# Assign a variable for the file to load and the path
file_to_load = os.path.join(cwd, "Resources", "election_results.csv")
#Open the file in read mode
#election_data = open(file_to_load, 'r')
#or
#with open(file_to_load, 'r') as election_data:
#to do Analysis
#print(election_data)
#Close file
# Open the election results and read the file
with open(file_to_load, 'r') as election_data:

     # To do: perform analysis.
    print(election_data)

   # for row in election_data:
       #  print(row) """
#import csv
#import os
# Assign a variable for the file to load and the path.
#file_to_load = os.path.join("Resources", "election_results.csv")
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
#with open(file_to_load) as election_data:
#open(file_to_save, 'w')
    # Print the file object.
 #    print(election_data)

# Assign a variable for the file to load and the path.
#file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # Print the file object.
   #  print(election_data)
   
   # Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")

# Close the file
#outfile.close()
# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
   #txt_file.write("Hello World")
    # Write three counties to the file.
     #txt_file.write("Arapaho, ")
     #txt_file.write("Denver, ")
     #txt_file.write("Jefferson")
     # Write three counties to the file.
    # txt_file.write("Counties in Election\n-------------------\nArapahoe\nDenver\nJefferson")

  # print(txt_file)
#file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file
#with open(file_to_load) as election_data:

     # To do: perform analysis.
     #print(election_data)

##------3.4.4 Read the elections results---------
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
totalVolume = 0 # set to zero before we open the file
candadite_options = [] #declare variable for our empty list
candidate_votes = {} #declare a variable for our empty dictionary
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data) # Read the file object with the reader function.
    headers = next(file_reader)
         # Print each row in the CSV file
    for row in file_reader:
        # 2. Add to the total vote count.
        totalVolume += 1
    #print(totalVolume) #print out count to determine total 
        candidate_name = row[2] # Print the candidate name from each row
        
        if candidate_name not in candadite_options: #check for name in dictionary
          candadite_options.append(candidate_name) # add name to dictionary
          candidate_votes[candidate_name] = 0 #Begin tracking that candidate's vote count.
        candidate_votes[candidate_name] += 1 # Add a vote to that candidate's count.
        #print(candidate_votes)
# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candadite_options:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(totalVolume) * 100
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
  # Determine winning vote count and candidate
    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # And, set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
