# expense_tracker.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load expenses from CSV
def load_expenses(file_path='expenses.csv'):
    try:
        df = pd.read_csv(file_path)
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

# Main Execution
def main():
    df = load_expenses()
    if df.empty:
        print("No data available.")
        return

    total_spending(df)
    summary = category_analysis(df)

    # Optional visual
    show_chart = input("\nShow pie chart? (y/n): ").lower()
    if show_chart == 'y':
        show_pie_chart(summary)

    # Optional export
    export = input("Export summary to CSV? (y/n): ").lower()
    if export == 'y':
        export_summary(summary)

if __name__ == "__main__":
    main()
