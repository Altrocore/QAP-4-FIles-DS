# Project 2 - show graph of total amount of sales for each month
# Author: Daniel Shepelev
# Created 23 March
# Updated 25 March

# Imports
import matplotlib.pyplot as plt

salesList = []
monthsList = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
for month in monthsList:
    sale = float(input(f"Enter total sales for {month}: "))
    salesList.append(sale)

# plot the graph
plt.plot(monthsList, salesList)

# add label and title
plt.xlabel("Month")
plt.ylabel("Total sales ($)")
plt.title("Total sales by month")

# show the graph
plt.show()
