from database import connect

def add_expense(type, amount, category, date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expenses (type, amount, category, date) VALUES (?, ?, ?, ?)",
        (type, amount, category, date)
    )
    conn.commit()
    conn.close()


def view_expenses():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()
    return rows


# ✅ NEW: Delete expense
def delete_expense(expense_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()


# ✅ NEW: Calculate balance
def calculate_balance():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses WHERE type='income'")
    income = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(amount) FROM expenses WHERE type='expense'")
    expense = cursor.fetchone()[0] or 0

    conn.close()

    return income - expense