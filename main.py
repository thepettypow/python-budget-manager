import sqlite3
from datetime import datetime

# DB init
conn = sqlite3.connect("budget.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY,
        amount REAL,
        category TEXT,
        date TEXT
    )
''')
conn.commit()

# funcs
def add_expense(amount, category):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)", (amount, category, date))
    conn.commit()
    print("Expense added successfully!")

def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    if expenses:
        for exp in expenses:
            print(f"Amount: {exp[1]}, Category: {exp[2]}, Date: {exp[3]}")
    else:
        print("No expenses recorded.")

def total_expenses():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]
    return total if total else 0

# main func
def main():
    print("Welcome to Personal Budget Manager!")
    while True:
        print("\nOptions:\n1. Add Expense\n2. View Expenses\n3. View Total Expenses\n4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            try:
                amount = float(input("Enter expense amount: "))
                category = input("Enter expense category (e.g., Food, Transport, Bills): ")
                add_expense(amount, category)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print(f"Total expenses: {total_expenses()}")
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()
