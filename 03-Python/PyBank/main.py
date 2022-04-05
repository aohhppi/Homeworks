# Import Statements
import csv
import os

# Create a path
# Files to load and output
budget_file = "Resources/budget_data.csv"
file_results = "analysis/budget_analysis.txt"

# Variables
total_months = 0
prev_profit = 0
month_of_change = []
profit_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999999]
total_profit = 0

# Read the csv and convert it into a list of dictionaries
with open(budget_file) as profit_data:
    reader = csv.DictReader(profit_data)

    for row in reader:

        # Track the total
        total_months = total_months + 1
        total_profit = total_profit + int(row["Profit/Losses"])

        # Track the proffit change
        profit_change = int(row["Profit/Losses"]) - prev_profit
        prev_profit = int(row["Profit/Losses"])
        profit_change_list = profit_change_list + [profit_change]
        month_of_change = month_of_change + [row["Date"]]

        # Calculate the greatest increase
        if (profit_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = profit_change

        # Calculate the greatest decrease
        if (profit_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = profit_change

# Calculate the Average
revenue_avg = sum(profit_change_list) / len(profit_change_list)

# Generate Output
output = (

    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit}\n"
    f"Average Change: ${revenue_avg}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    )

# Print the output
print(output)

# Export the results to text file
with open(file_results, "w") as txt_file:
    txt_file.write(output)
    

   
