print("SALES ANALYSIS")
print("MONTHLY  SALES  REPORT")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#           ------------- read sales data-------------------
df=pd.read_csv("sales_analyzer.csv")
print(df.to_string())
df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')
df['year']=df['Order_Date'].dt.year
df['month']=df['Order_Date'].dt.month
df['date'] = df['Order_Date'].dt.date    
print(df)

#         ------------getting month details from user---------------
month_num = int(input("Enter month number (1-12): "))

months = ["Jan", "Feb", "Mar", "Apr", "May", "June",
          "July", "Aug", "Sep", "Oct", "Nov", "Dec"]

if 1 <= month_num <= 12:
    print("Selected Month:", months[month_num - 1])
else:
    print("Invalid month number")

    #       ------------ Filter data for selected month---------------
monthly_df = df[df['month'] == month_num]

if monthly_df.empty:
    print("No data available for the selected month.")
else:
    print("\n📊 MONTHLY SALES REPORT\n")

    #            ------------ Category-wise sales------------
    category_sales = monthly_df.groupby('Category')['Order_ID'].count()
    print("Category-wise Sales:")
    print(category_sales, "\n")

    #            ------------Category-wise revenue--------------
    category_revenue = monthly_df.groupby('Category')['Revenue'].sum()
    print("Category-wise Revenue:")
    print(category_revenue, "\n")

    #           --------------Total sales of the month------------
    total_sales = monthly_df['Order_ID'].count()
    print("Total Sales of the Month:", total_sales, "\n")

    #              -----------Date with highest sales-------------
    daily_sales = monthly_df.groupby('date')['Order_ID'].count()
    print(daily_sales)
    highest_sale_date = daily_sales.idxmax()
    lowest_sale_date = daily_sales.idxmin()

    print("Date with Highest Sales:", highest_sale_date)
    print("Date with Lowest Sales:", lowest_sale_date)

    #               -------- BAR CHART: CATEGORY-WISE SALES --------
    category_sales.plot(kind='bar', figsize=(7,5))
    plt.title("Category-wise Sales")
    plt.xlabel("Category")
    plt.ylabel("Number of Orders")
    plt.tight_layout()
    plt.show()

    #               -------- BAR CHART: CATEGORY-WISE REVENUE --------
    category_revenue.plot(kind='bar', figsize=(7,5))
    plt.title("Category-wise Revenue")
    plt.xlabel("Category")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.show()


    #-----------------------------------------------------------------------END OF THE MONTHLY REPORT---------------------------------------------------------------------