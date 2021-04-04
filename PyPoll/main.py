# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
#You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

  #* The total number of votes cast

  #* A complete list of candidates who received votes

  #* The percentage of votes each candidate won

  #* The total number of votes each candidate won

  #* The winner of the election based on popular vote.


#Import os Module
import os
#Import csv for reading
import csv

csvpath = os.path.join('Resources','election_data.csv')

#variables
votes = []
candidates = []

#Read CSV File

with open(csvpath, 'r') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
   csvreader = csv.reader(csvfile, delimiter = ',')
    # Read the header row first (skip this step if there is no header)
   csv_header = next(csvreader)
    # Read the header row first (skip this step if there is no header)

   for column in csvreader:
       votes.append(column[0])
       candidates.append(column[2])

   Total_Votes = (len(votes))
   print(f"Total Votes: {Total_Votes}")
   #Count each number of candidates in the candidates list
   Khan = int(candidates.count("Khan"))
   Correy = int(candidates.count("Correy"))
   Li = int(candidates.count("Li"))
   O_Tooley = int(candidates.count("O'Tooley"))
   #Get a percentage of each candidates vote total
   Khan_percentage = format(((Khan/Total_Votes) * 100),'.3f')
   Correy_percentage = format(((Correy/Total_Votes) * 100),'.3f')
   Li_percentage = format(((Li/Total_Votes) * 100),'.3f')
   O_Tooley_percentage = format(((O_Tooley/Total_Votes) * 100),'.3f')
   #Print each candidate's name, vote percentage, and raw number of votes
   print("----------------------------------------------------------")
   print("Election Results")
   print("----------------------------------------------------------")
   print(f"Khan: {Khan_percentage}% ({Khan})")
   print(f"Correy: {Correy_percentage}% ({Correy})")
   print(f"Li: {Li_percentage}% ({Li})")
   print(f"O'Tooley: {O_Tooley_percentage}% ({O_Tooley})")
   print("----------------------------------------------------------")
    #Compare Votes and pick winner with the most votes
   if Khan > Correy > Li > O_Tooley:
       Winner = "Khan"
   elif Correy > Khan > Li > O_Tooley:
       Winner = "Correy"
   elif Li > Khan > Correy > O_Tooley:
       Winner = "Li"
   elif O_Tooley > Khan > Correy > Li:
       Winner = "O'Tooley"
   print(f"Winner: {Winner}")
   print("-------------------------")

with open('election_Results.txt', 'w') as text:
   text.write("----------------------------------------------------------\n")
   text.write("Election Results"+ "\n")
   text.write("----------------------------------------------------------\n")
   text.write(f"Total Votes: {Total_Votes}" + "\n")
   text.write(f"Khan: {Khan_percentage}% ({Khan})" + "\n")
   text.write(f"Correy: {Correy_percentage}% ({Correy})" + "\n")
   text.write(f"Li: {Li_percentage}% ({Li})" + "\n")
   text.write(f"O'Tooley: {O_Tooley_percentage}% ({Correy})" + "\n")
   text.write("----------------------------------------------------------\n")
   text.write(f"Winner: {Winner}" + "\n")
   text.write("----------------------------------------------------------\n")
   
