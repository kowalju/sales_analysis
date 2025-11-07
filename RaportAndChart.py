import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

file_path = os.path.join(r'C:\Users\julia\Documents\Python', 'sales.csv')

df = pd.read_csv(file_path)

df['value'] = df['price']* df['quantity']

sales_by_product = df.groupby('name')['value'].sum().sort_values(ascending=False)
sales_by_product.index.name = None

df['date'] = pd.to_datetime(df['date'])
sales_by_day = df.groupby('date')['value'].sum()

plt.figure(figsize=(8,5))
plt.plot(sales_by_day.index, sales_by_day.values, marker='o')
plt.title('Daily sales: (in PLN)')
plt.xlabel('Date')
plt.ylabel('Sales value [PLN]')
plt.grid(True)
plt.tight_layout()
plt.savefig('sales_chart.png')
plt.close()

total_sales = df['value'].sum()
best_product = sales_by_product.idxmax()
best_value = round(sales_by_product.max(),2)

with open("sales_report.txt", "w", encoding="utf-8") as f:
    f.write("SALES REPORT\n")
    f.write("====================\n")
    f.write(f"Total value of sales: {total_sales:.2f} PLN\n")
    f.write(f"Best selling product: {best_product} ({best_value:.2f} PLN)\n\n")
    f.write("Sales by product:\n")
    f.write(sales_by_product.to_string())

print("Raport generated: sales_report.txt i sales_chart.png")
