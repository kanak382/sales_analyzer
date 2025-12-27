print("SALES ANALYSIS")
print("ANNUAL  SALES  REPORT")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#         -----------read sales data-------------------
df=pd.read_csv("sales_analyzer.csv")
print(df.to_string())
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['year']=df['Order_Date'].dt.year
df['month']=df['Order_Date'].dt.month
df['Month_Num'] = df['Order_Date'].dt.month  
print(df)

#       ---------------show monthly sales-------------
print("monthly sales")
monthly_sales = df.groupby('Month_Num')['Order_ID'].count()
print(monthly_sales)

#             -----------month with highest sales---------------
highest_sales_month = monthly_sales.idxmax()
print("Month with Highest Sales:", highest_sales_month)

#              -----------monthly revenue ---------------
print("monthly revenue")
monthly_revenue = df.groupby('Month_Num')['Order_ID'].count()
print(monthly_revenue)
#              ------month with highest revenue------
highest_revenue_month = monthly_revenue.idxmax()
print("\nMonth with Highest Revenue:", highest_revenue_month)

#            ----------- cateegory wise sales for each month-----------
category_month_sales = df.groupby(['Month_Num','Category'])['Order_ID'].count()
print("\nCategory-wise Sales for Each Month:")
print(category_month_sales)
#            -----------bar plot for monthly sales--------------
plt.figure(figsize=(10,6))
monthly_sales.plot(kind='bar', color='skyblue')
plt.title("Total Sales Per Month")
plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
plt.show()

#           ----------- bar graph for category wise sales per month-------------
category_month_sales.plot(kind='bar', figsize=(10,6))
plt.title('Category-wise Sales per Month')
plt.ylabel('Number of Orders')
plt.show()

#         -------------revenue distribution----------
monthly_revenue = df.groupby('Month_Num')['Revenue'].sum()
plt.figure(figsize=(8,6))
plt.pie(
    monthly_revenue,
    labels=monthly_revenue.index,
    autopct='%1.1f%%',
    startangle=140
)
plt.title('Monthly Revenue Distribution')
plt.show()

# line chart for annual trends
monthly_sales = (df.groupby(['Month_Num', 'month'])['Sales_Quantity'].sum().reset_index())
monthly_sales = monthly_sales.sort_values('Month_Num')
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales['month'],monthly_sales['Sales_Quantity'],marker='o')
plt.title(f"Monthly Sales Pattern for the year")
plt.xlabel("Month")
plt.ylabel("Total Sales Quantity")
plt.grid(True)
plt.show()


    #-----------------------------------------------------------------------END OF THE ANNUAL REPORT---------------------------------------------------------------------
