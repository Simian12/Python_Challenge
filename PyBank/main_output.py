import os
import csv

Filepath="C:\\Users\\Banni\\Desktop\\Python_Challenge\\PyBank\\Resources\\budget_data.csv"
OutputFilepath = "C:\\Users\\Banni\\Desktop\\Python_Challenge\\PyBank\\Analysis\\financial_analysis.txt"
#variables
total_months=0
net_total=0
prev_profit=0
changes=[]
dates=[]

with open(Filepath, newline="") as csvfile:
    csv_file=csv.DictReader(csvfile)

    for row in csv_file:
        date=row["Date"]
        profit_losses=int(row["Profit/Losses"])

        #Total Months and Net Total
        total_months += 1
        net_total += profit_losses

        #changes in profit/losses
        if total_months>1:
            change= profit_losses-prev_profit
            changes.append(change)
            dates.append(date)
    prev_profit=profit_losses

#Average Change
average_change=sum(changes)/(total_months)

#Greatest Increase and Decrease
max_increase=max(changes)
max_decrease=min(changes)

date_increase=dates[changes.index(max_increase)]
date_decrease=dates[changes.index(max_decrease)]

with open(OutputFilepath, 'w') as output_file:
    # Write the analysis results to the file
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {date_increase} (${max_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {date_decrease} (${max_decrease})\n")

print(f"Final_output{OutputFilepath}")