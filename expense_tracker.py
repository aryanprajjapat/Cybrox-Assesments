# expense_tracker.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Load expenses from CSV
def load_expenses(file_path='expenses.csv'):
    try:
        df = pd.read_csv(file_path, parse_dates=['Date'])
        return df
    except Exception as e:
        print(f"Error loading file: {e}")
        return pd.DataFrame()

# Total spending overview
def total_spending(df):
    total = df['Amount'].sum()
    max_expense = df.loc[df['Amount'].idxmax()]
    min_expense = df.loc[df['Amount'].idxmin()]
    print("\nTotal Spending Overview")
    print("------------------------")
    print(f"Total Spent: ₹{total}")
    print(f"Highest Expense: ₹{max_expense['Amount']} - {max_expense['Category']} ({max_expense['Description']})")
    print(f"Lowest Expense: ₹{min_expense['Amount']} - {min_expense['Category']} ({min_expense['Description']})")

# Category-wise analysis
def category_analysis(df):
    print("\nCategory-wise Analysis")
    print("------------------------")
    category_group = df.groupby('Category')['Amount'].agg(['sum', 'count'])
    category_group.columns = ['Total_Spent', 'Transactions']
    category_group['Percentage'] = round((category_group['Total_Spent'] / df['Amount'].sum()) * 100, 2)
    print(category_group)
    return category_group

# Bonus: Visualize data as pie chart
def show_pie_chart(category_group):
    plt.figure(figsize=(6, 6))
    plt.pie(category_group['Total_Spent'], labels=category_group.index, autopct='%1.1f%%')
    plt.title('Expense Distribution by Category')
    plt.show()

# Bonus: Export summary to CSV
def export_summary(category_group, filename='summary_report.csv'):
    category_group.to_csv(filename)
    print(f"Summary exported to {filename}")

# Bonus: Filter by date range
def filter_by_date(df):
    try:
        start = input("Enter start date (YYYY-MM-DD): ")
        end = input("Enter end date (YYYY-MM-DD): ")
        start_date = pd.to_datetime(start)
        end_date = pd.to_datetime(end)
        filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
        print(f"Filtered {len(filtered_df)} records from {start} to {end}.")
        return filtered_df
    except Exception as e:
        print("Invalid date format or error in filtering.", e)
        return df

# Bonus: Add new expense dynamically
def add_expense(df, file_path='expenses.csv'):
    try:
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        new_data = pd.DataFrame([[date, category, amount, description]], columns=['Date', 'Category', 'Amount', 'Description'])
        new_data['Date'] = pd.to_datetime(new_data['Date'])
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv(file_path, index=False)
        print("Expense added successfully.")
    except Exception as e:
        print("Error adding expense:", e)
    return df

# Main Execution
def main():
    df = load_expenses()
    if df.empty:
        print("No data available.")
        return

    while True:
        print("\nWhat would you like to do?")
        print("1. View Total and Category Summary")
        print("2. Filter Expenses by Date Range")
        print("3. Add a New Expense")
        print("4. Show Pie Chart")
        print("5. Export Summary to CSV")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            total_spending(df)
            summary = category_analysis(df)
        elif choice == '2':
            df = filter_by_date(df)
        elif choice == '3':
            df = add_expense(df)
        elif choice == '4':
            summary = category_analysis(df)
            show_pie_chart(summary)
        elif choice == '5':
            summary = category_analysis(df)
            export_summary(summary)
        elif choice == '6':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 6.")

if __name__ == "__main__":
    main()