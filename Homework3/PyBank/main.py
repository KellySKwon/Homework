#Homework #3 - pybank

#import libraries
import os
import csv

#create object path for csv file
budget_data = os.path.join("budget_data.csv")

#declare variables and lists to hold values
monTotal = 0    
netTotal = 0
netChange = 0
dateCart = []
profitCart = []
changeCart = []

#read CSV file
with open(budget_data,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    #set header row (skips header in counts)
    header = next(csvreader)
    
    #loops through csv rows
    for row in csvreader:
        #count # of months (counting rows)
        monTotal +=1

        #hold dates
        dateCart.append(row[0])
        #hold profit/losses
        profitCart.append(int(row[1]))
        
        #net total (sum profit/loss column)
        netTotal += int(row[1])
        
    #profit/loss change from previous row
    for profitRow in range(1,monTotal): 
        changeCart.append(profitCart[profitRow] - profitCart[profitRow-1])
    
    #average change in "profits/losses"
    changeAvg = round(sum(changeCart)/len(changeCart),2)
    
    #greatest increase in profits
    maxChange = round(max(changeCart),2)
    #hold index row of maxChange
    maxIndex = changeCart.index(maxChange)

    #greatest decrease in profits
    minChange = round(min(changeCart),2)
    #hold index row of minChange
    minIndex = changeCart.index(minChange)

#print results to terminal
print('Financial Analysis\n----------------------------------')
print(f'Total Months: {monTotal}')
print(f'Total: ${netTotal}')
print(f'Average Change: ${changeAvg}')
print(f'Greatest Increase: in Profits: {dateCart[maxIndex+1]} ${maxChange}')
print(f'Greatest Decrease in Profits: {dateCart[minIndex+1]} ${minChange}')

#export and write results to output.txt
output = open("output.txt","w")

output.write('Financial Analysis\n---------------------------------\n')
output.write(f'Total Months: {monTotal}\n')
output.write(f'Total: ${netTotal}\n')
output.write(f'Average Change: ${changeAvg}\n')
output.write(f'Greatest Increase: in Profits: {dateCart[maxIndex+1]} ${maxChange}\n')
output.write(f'Greatest Decrease in Profits: {dateCart[minIndex+1]} ${minChange}')
