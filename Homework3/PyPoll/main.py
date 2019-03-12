#Homework #3 - pypoll

#import libraries
import os
import csv

#create object path for csv file
election_data = os.path.join("election_data.csv")

#declare variables and lists to hold values
votesTotal = 0
candidatesCart = []
candidatesUnique = []
candidatesVote = []
votesPercentage = []

#read CSV file
with open(election_data,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    #set header row (skips header in counts)
    header = next(csvreader)

    #loops through csv rows
    for row in csvreader:
        #count total number of votes cast (counting rows)
        votesTotal +=1
        #hold candidates
        candidatesCart.append(row[2])
    
    #sets do not have duplicates so create a set for unique candidate names (however, it's unordered)
    for candidates in set(candidatesCart):
        #create list of unqiue candidates
        candidatesUnique.append(candidates)
        #count votes for each candidate
        candidatesCnt = candidatesCart.count(candidates)
        #create list of vote counts
        candidatesVote.append(candidatesCnt)
        #calculate % of votes for each candidate
        votesCalc = round((candidatesCnt/votesTotal)*100,2)
        #create list of percentage of votes
        votesPercentage.append(str(votesCalc)+"%")

    
    #combine candidate name and their metrics to a list using zip function
    #need to convert set to a list to get index of items
    voteResult = list(zip(candidatesUnique,votesPercentage,candidatesVote))

    #find candidate with max number of votes
    for i in voteResult:    
        if max(candidatesVote) == i[2]:
            winner = i[0]
        

#print results
print('Election Results\n------------------------')
print(f'Total Votes: {votesTotal}\n------------------------')
print(f'{voteResult[0][0]}: {voteResult[0][1]} ({voteResult[0][2]})')
print(f'{voteResult[1][0]}: {voteResult[1][1]} ({voteResult[1][2]})')
print(f'{voteResult[2][0]}: {voteResult[2][1]} ({voteResult[2][2]})')
print(f'{voteResult[3][0]}: {voteResult[3][1]} ({voteResult[3][2]})')
print('------------------------')
print(f'Winner: {winner}')

#export and write results to output.txt
output = open("output.txt","w")
output.write('Election Results\n------------------------\n')
output.write(f'Total Votes: {votesTotal}\n------------------------\n')
output.write(f'{voteResult[0][0]}: {voteResult[0][1]} ({voteResult[0][2]})\n')
output.write(f'{voteResult[1][0]}: {voteResult[1][1]} ({voteResult[1][2]})\n')
output.write(f'{voteResult[2][0]}: {voteResult[2][1]} ({voteResult[2][2]})\n')
output.write(f'{voteResult[3][0]}: {voteResult[3][1]} ({voteResult[3][2]})\n')
output.write('------------------------\n')
output.write(f'Winner: {winner}')