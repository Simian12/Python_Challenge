import os
import csv

Filepath="C:\\Users\\Banni\\Desktop\\Python_Challenge\\PyBank\\Resources\\budget_data.csv"

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

#Final Prints
print("Financial Analysis")
print("---------------------")
print(f"Total_Months:{total_months}")
print(f"Total_Net:${net_total}")
print(f"Average_Change:${round(average_change,2)}")
print(f"Greatest_Increase:{date_increase}(${max_increase})")
print(f"Greatest Decrease:{date_decrease}(${max_decrease})")

  
