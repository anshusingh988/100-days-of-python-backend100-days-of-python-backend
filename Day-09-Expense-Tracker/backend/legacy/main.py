from database import create_table
from expense import add_expense, view_expenses, delete_expense, calculate_balance

create_table()

while True:
    try:
        print("\n====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Show Balance")
        print("5. Exit")

        choice = input("Enter choice: ")

        # 🔹 Add Expense
        if choice == "1":
            type = input("Type (income/expense): ")
            amount = float(input("Amount: "))
            category = input("Category: ")
            date = input("Date: ")

            add_expense(type, amount, category, date)
            print("✅ Added successfully!")

        # 🔹 View Expenses
        elif choice == "2":
            data = view_expenses()
            print("\n--- All Transactions ---")
            for row in data:
                print(f"ID: {row[0]} | Type: {row[1]} | Amount: {row[2]} | Category: {row[3]} | Date: {row[4]}")

        # 🔹 Delete Expense
        elif choice == "3":
            expense_id = int(input("Enter ID to delete: "))
            delete_expense(expense_id)
            print("❌ Deleted successfully!")

        # 🔹 Show Balance
        elif choice == "4":
            balance = calculate_balance()
            print(f"💰 Current Balance: {balance}")

        # 🔹 Exit
        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice")

    except KeyboardInterrupt:
        print("\n⚠️ Program interrupted")