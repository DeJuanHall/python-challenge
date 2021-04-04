#create a Python script that analyzes the records to calculate each of the following:
    #The total number of months included in the dataset
    #The net total amount of "Profit/Losses" over the entire period
    #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in losses (date and amount) over the entire period

#import dependencies
import os
import csv

# Define File Path
budgetcsv = os.path.join('Resources', 'budget_data.csv')

# Define Varibles for PyBank Analysis
profit = []
monthly_changes = []
date = []

Month_count = 0
total_profit = 0
total_profit_change = 0
initial_profit = 0

# Read CSV File Data
with open(budgetcsv, "r") as csvfile:
    # name delimeter as comma
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Count of months
    for row in csvreader:    
      Month_count = Month_count + 1 

      # used to calculate the greatest increase and decrease in profits
      date.append(row[0])

      # Append the profit information / calculate the total profit
      profit.append(row[1])
      total_profit = total_profit + int(row[1])

      #Calculate the average change in profits month over month. Calulate the average change in profits
      final_profit = int(row[1])
      monthly_change_profits = final_profit - initial_profit

      #Store these monthly changes in a list
      monthly_changes.append(monthly_change_profits)

      total_profit_change = total_profit_change + monthly_change_profits
      initial_profit = final_profit

      #Calculate the average change in profit
      average_change_profits = (total_profit_change/Month_count)
      
      #Find the max and min change in profit and dates for changes
      greatest_increase_profits = max(monthly_changes)
      greatest_decrease_profits = min(monthly_changes)

      increase_date = date[monthly_changes.index(greatest_increase_profits)]
      decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
      
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(Month_count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")

with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(Month_count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")