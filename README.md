# Expense Tracker 🧾

This is a simple Python program that helps you keep track of your daily expenses. It reads your expense data from a CSV file and gives you a summary of how much you're spending, where you're spending it, and even shows a pie chart if you want.



- 📥 Read expenses from a CSV file (like an Excel sheet)
- 💰 Show how much money you spent in total
- 🔍 Find out your biggest and smallest expenses
- 📊 Break down spending by category:
  - Total money spent in each category
  - How many times you spent in each category
  - What percent of your total spending went to each category
- 🥧 (Optional) Show a pie chart of spending by category
- 📤 Save the summary to a new file called `summary_report.csv`


``
ExpenseTracker/
├── expense_tracker.py         # The main Python file
├── expenses.csv               # Your input data (you create this)
└── summary_report.csv         # Summary file (created automatically)
```

1. **Install the required libraries:**
```bash
pip install pandas numpy matplotlib
```

2. **Create your `expenses.csv` file** with this data:
```csv
Date,Category,Amount,Description
2025-06-10,Food,150,Pizza at Dominos
2025-06-11,Transport,50,Rickshaw fare
2025-06-12,Rent,5000,June Rent
2025-06-12,Utilities,200,Electricity Bill
```

3. **Run the Python script:**
```bash
python expense_tracker.py
```

4. **Follow the prompts:**
- Type **y** if you want to see the pie chart
- Type **y** again if you want to save the report as a CSV file

---

## 💡 Sample Output
```
Total Spending Overview
------------------------
Total Spent: ₹5400
Highest Expense: ₹5000 - Rent (June Rent)
Lowest Expense: ₹50 - Transport (Rickshaw fare)

Category-wise Analysis
------------------------
           Total Spent  Transactions  Percentage
Category                                        
Food               150             1         2.78
Rent              5000             1        92.59
Transport           50             1         0.93
Utilities          200             1         3.70
```

---

## 🎁 Extra Features
- 🥧 Pie chart to visualize your spending
- 📤 Option to save a summary file

---

## ⚠️ Limitations / Future Ideas
- Right now, it doesn’t filter by date — that could be added
- It works in the terminal (not a website or app)
- Basic error handling — needs improvement for real use

---

## 🛠 Tools Used
- Python
- Pandas
- NumPy
- Matplotlib (for charts)

---

**Author:** Aryan Prajapat  
**Date:** 2025-06-20
