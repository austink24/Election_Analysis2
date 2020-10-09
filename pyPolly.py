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

##3.4.4 Read the elections results
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
      # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

         # Print each row in the CSV file
#    for row in file_reader:
#        print(row)
# Print the header row.
    headers = next(file_reader)
    print(headers)