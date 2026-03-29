<<<<<<< HEAD
import tkinter as tk
from tkinter import messagebox
from database import init_db, add_task, get_tasks, complete_task, delete_task
from ai_service import analyze_task

# Initialize DB
init_db()

# Create window
root = tk.Tk()
root.title("AI To-Do App")
root.geometry("600x500")
root.config(bg="#1e1e1e")

# ===== FUNCTIONS =====

def refresh_tasks():
    listbox.delete(0, tk.END)
    tasks = get_tasks()
    for task in tasks:
        t_id, title, category, priority, status, parent_id = task
        display = f"{t_id}. {title} [{category} | {priority} | {status}]"
        listbox.insert(tk.END, display)

def add_new_task():
    title = entry.get()
    if not title:
        messagebox.showwarning("Warning", "Enter a task!")
        return

    ai_result = analyze_task(title)
    category = ai_result['category']
    priority = ai_result['priority']

    task_id = add_task(title, category, priority)

    # Add subtasks
    for sub in ai_result['subtasks']:
        add_task(sub, category, priority, parent_id=task_id)

    entry.delete(0, tk.END)
    refresh_tasks()

def mark_done():
    try:
        selected = listbox.get(listbox.curselection())
        task_id = int(selected.split(".")[0])
        complete_task(task_id)
        refresh_tasks()
    except:
        messagebox.showerror("Error", "Select a task!")

def delete_selected():
    try:
        selected = listbox.get(listbox.curselection())
        task_id = int(selected.split(".")[0])
        delete_task(task_id)
        refresh_tasks()
    except:
        messagebox.showerror("Error", "Select a task!")

# ===== UI DESIGN =====

title_label = tk.Label(root, text="🔥 AI To-Do App", font=("Arial", 18, "bold"), bg="#1e1e1e", fg="white")
title_label.pack(pady=10)

entry = tk.Entry(root, width=40, font=("Arial", 14))
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_new_task, bg="green", fg="white", width=15)
add_btn.pack(pady=5)

listbox = tk.Listbox(root, width=70, height=15, font=("Arial", 10))
listbox.pack(pady=10)

done_btn = tk.Button(root, text="Mark Done", command=mark_done, bg="blue", fg="white", width=15)
done_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", command=delete_selected, bg="red", fg="white", width=15)
delete_btn.pack(pady=5)

# Load tasks initially
refresh_tasks()

# Run app
=======
import tkinter as tk
from tkinter import messagebox
from database import init_db, add_task, get_tasks, complete_task, delete_task
from ai_service import analyze_task

# Initialize DB
init_db()

# Create window
root = tk.Tk()
root.title("AI To-Do App")
root.geometry("600x500")
root.config(bg="#1e1e1e")

# ===== FUNCTIONS =====

def refresh_tasks():
    listbox.delete(0, tk.END)
    tasks = get_tasks()
    for task in tasks:
        t_id, title, category, priority, status, parent_id = task
        display = f"{t_id}. {title} [{category} | {priority} | {status}]"
        listbox.insert(tk.END, display)

def add_new_task():
    title = entry.get()
    if not title:
        messagebox.showwarning("Warning", "Enter a task!")
        return

    ai_result = analyze_task(title)
    category = ai_result['category']
    priority = ai_result['priority']

    task_id = add_task(title, category, priority)

    # Add subtasks
    for sub in ai_result['subtasks']:
        add_task(sub, category, priority, parent_id=task_id)

    entry.delete(0, tk.END)
    refresh_tasks()

def mark_done():
    try:
        selected = listbox.get(listbox.curselection())
        task_id = int(selected.split(".")[0])
        complete_task(task_id)
        refresh_tasks()
    except:
        messagebox.showerror("Error", "Select a task!")

def delete_selected():
    try:
        selected = listbox.get(listbox.curselection())
        task_id = int(selected.split(".")[0])
        delete_task(task_id)
        refresh_tasks()
    except:
        messagebox.showerror("Error", "Select a task!")

# ===== UI DESIGN =====

title_label = tk.Label(root, text="🔥 AI To-Do App", font=("Arial", 18, "bold"), bg="#1e1e1e", fg="white")
title_label.pack(pady=10)

entry = tk.Entry(root, width=40, font=("Arial", 14))
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_new_task, bg="green", fg="white", width=15)
add_btn.pack(pady=5)

listbox = tk.Listbox(root, width=70, height=15, font=("Arial", 10))
listbox.pack(pady=10)

done_btn = tk.Button(root, text="Mark Done", command=mark_done, bg="blue", fg="white", width=15)
done_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", command=delete_selected, bg="red", fg="white", width=15)
delete_btn.pack(pady=5)

# Load tasks initially
refresh_tasks()

# Run app
>>>>>>> origin/main
root.mainloop()