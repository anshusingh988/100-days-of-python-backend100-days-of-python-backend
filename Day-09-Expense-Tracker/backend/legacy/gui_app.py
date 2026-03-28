import tkinter as tk
from tkinter import messagebox
from expense import add_expense, view_expenses, delete_expense, calculate_balance
from database import create_table

create_table()

# 🎨 Colors
BG_COLOR = "#1e1e2f"
CARD_COLOR = "#2c2c3e"
BTN_COLOR = "#4CAF50"
TEXT_COLOR = "white"

# 🖥️ Main Window
root = tk.Tk()
root.title("Expense Tracker Pro")
root.geometry("700x550")
root.config(bg=BG_COLOR)

# 🔹 Title
title = tk.Label(root, text="💰 Expense Tracker", font=("Arial", 20, "bold"), bg=BG_COLOR, fg="white")
title.pack(pady=10)

# 🔹 Card Frame
frame = tk.Frame(root, bg=CARD_COLOR, bd=0)
frame.pack(pady=10, padx=20, fill="x")

# 🔹 Input Fields
def create_label(text, row):
    tk.Label(frame, text=text, bg=CARD_COLOR, fg=TEXT_COLOR, font=("Arial", 11)).grid(row=row, column=0, padx=10, pady=8, sticky="w")

def create_entry(row):
    e = tk.Entry(frame, width=25, bd=0, font=("Arial", 11))
    e.grid(row=row, column=1, padx=10, pady=8)
    return e

create_label("Type", 0)
type_entry = create_entry(0)

create_label("Amount", 1)
amount_entry = create_entry(1)

create_label("Category", 2)
category_entry = create_entry(2)

create_label("Date", 3)
date_entry = create_entry(3)

# 🔹 Functions
def add():
    try:
        t = type_entry.get()
        amt = float(amount_entry.get())
        cat = category_entry.get()
        date = date_entry.get()

        add_expense(t, amt, cat, date)
        messagebox.showinfo("Success", "✅ Added successfully!")
        clear_fields()
        show()
    except:
        messagebox.showerror("Error", "Invalid input")

def show():
    listbox.delete(0, tk.END)
    for row in view_expenses():
        listbox.insert(tk.END, f"{row[0]} | {row[1]} | ₹{row[2]} | {row[3]} | {row[4]}")

def delete():
    try:
        selected = listbox.get(listbox.curselection())
        expense_id = int(selected.split("|")[0].strip())
        delete_expense(expense_id)
        messagebox.showinfo("Deleted", "❌ Deleted successfully!")
        show()
    except:
        messagebox.showerror("Error", "Select an item first")

def balance():
    bal = calculate_balance()
    messagebox.showinfo("Balance", f"💰 Balance: ₹{bal}")

def clear_fields():
    type_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

# 🔹 Buttons
btn_frame = tk.Frame(root, bg=BG_COLOR)
btn_frame.pack(pady=15)

def create_btn(text, cmd, color):
    return tk.Button(btn_frame, text=text, command=cmd, width=12,
                     bg=color, fg="white", bd=0, font=("Arial", 10, "bold"),
                     activebackground=color)

create_btn("Add", add, "#4CAF50").grid(row=0, column=0, padx=5)
create_btn("Show", show, "#2196F3").grid(row=0, column=1, padx=5)
create_btn("Delete", delete, "#f44336").grid(row=0, column=2, padx=5)
create_btn("Balance", balance, "#FF9800").grid(row=0, column=3, padx=5)

# 🔹 Listbox Frame
list_frame = tk.Frame(root, bg=CARD_COLOR)
list_frame.pack(padx=20, pady=10, fill="both", expand=True)

listbox = tk.Listbox(list_frame, bg="#121212", fg="white",
                     font=("Consolas", 10), bd=0)
listbox.pack(fill="both", expand=True, padx=10, pady=10)

# Run App
root.mainloop()

def show_chart():
    data = view_expenses()

    categories = {}
    for row in data:
        if row[1] == "expense":  # only expenses
            cat = row[3]
            amt = row[2]
            categories[cat] = categories.get(cat, 0) + amt

    if not categories:
        messagebox.showinfo("Info", "No expense data to show")
        return

    plt.figure()
    plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%')
    plt.title("Expense Distribution")
    plt.show()