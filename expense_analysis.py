import csv
import numpy as np
import matplotlib.pyplot as plt

dates = []
categories = []
amounts = []

print("Program started")

with open("expenses.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    print("Header:", header)

    for row in reader:
        print("Row read:", row)
        dates.append(row[0])
        categories.append(row[1])
        amounts.append(float(row[2]))

print("CSV loaded successfully")
print("Amounts list:", amounts)

amounts_np = np.array(amounts)

total_expense = np.sum(amounts_np)
average_expense = np.mean(amounts_np)
median_expense = np.median(amounts_np)

print("Total Expense:", total_expense)
print("Average Expense:", average_expense)
print("Median Expense:", median_expense)

print("High Expenses (above 1000):")
for i in range(len(amounts_np)):
    if amounts_np[i] > 1000:
        print(dates[i], categories[i], amounts_np[i])


category_totals = {}

for i in range(len(categories)):
    if categories[i] in category_totals:
        category_totals[categories[i]] += amounts_np[i]
    else:
        category_totals[categories[i]] = amounts_np[i]

print(category_totals)

plt.bar(category_totals.keys(), category_totals.values())
plt.title("Category-wise Expenses")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.show()

plt.plot(dates, amounts_np, marker='o')
plt.title("Expense Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.show()
