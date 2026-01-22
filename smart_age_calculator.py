import tkinter as tk
from tkinter import messagebox, ttk
from datetime import date
import winsound
import random

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Smart Age Calculator")
root.geometry("480x650")
root.configure(bg="#0f2027")
root.resizable(False, False)

# ---------------- SOUNDS ----------------
def sound_success():
    winsound.Beep(1200, 200)

def sound_error():
    winsound.Beep(600, 300)

# ---------------- AGE CALCULATION ----------------
def calculate_age():
    try:
        y = int(year_entry.get())
        m = int(month_entry.get())
        d = int(day_entry.get())

        dob = date(y, m, d)
        today = date.today()

        if dob > today:
            sound_error()
            messagebox.showerror("Error", "DOB cannot be in future")
            return

        # Accurate age
        years = today.year - dob.year
        months = today.month - dob.month
        days = today.day - dob.day

        if days < 0:
            months -= 1
            days += 30
        if months < 0:
            years -= 1
            months += 12

        total_days = (today - dob).days

        # Next birthday
        next_bday = date(today.year, dob.month, dob.day)
        if next_bday < today:
            next_bday = date(today.year + 1, dob.month, dob.day)
        days_left = (next_bday - today).days

        # Year progress
        year_start = date(today.year, dob.month, dob.day)
        if year_start > today:
            year_start = date(today.year - 1, dob.month, dob.day)

        year_progress = ((today - year_start).days / 365) * 100
        progress_bar["value"] = year_progress

        result_label.config(
            text=f"""
🎉 AGE DETAILS 🎉

🧓 {years} Years
📆 {months} Months
📅 {days} Days

📊 Total Days Lived : {total_days}

🎂 Next Birthday In
⏳ {days_left} Days
""",
            fg="#00ffea"
        )

        sound_success()
        show_quiz(years)

    except:
        sound_error()
        messagebox.showerror("Error", "Enter valid DOB")

# ---------------- QUIZ ----------------
quiz_data = {
    "adult": [
        ("Best backend language?", "Python", ["Python", "HTML", "CSS"]),
        ("What does API stand for?", "Interface", ["Interface", "Internet", "Input"])
    ],
    "student": [
        ("Most important for coding?", "Maths", ["Maths", "History", "Geography"]),
        ("Binary of 1?", "1", ["1", "0", "10"])
    ]
}

def show_quiz(age):
    quiz_frame.pack(pady=10)

    category = "adult" if age >= 18 else "student"
    q, ans, options = random.choice(quiz_data[category])

    quiz_q.config(text=q)

    def check(choice):
        if choice == ans:
            quiz_result.config(text="✅ Correct Answer!", fg="#00ff88")
            sound_success()
        else:
            quiz_result.config(text="❌ Wrong Answer!", fg="#ff6b6b")
            sound_error()

    btn1.config(text=options[0], command=lambda: check(options[0]))
    btn2.config(text=options[1], command=lambda: check(options[1]))
    btn3.config(text=options[2], command=lambda: check(options[2]))

# ---------------- RESET ----------------
def reset_app():
    year_entry.delete(0, tk.END)
    month_entry.delete(0, tk.END)
    day_entry.delete(0, tk.END)
    result_label.config(text="")
    quiz_frame.pack_forget()
    progress_bar["value"] = 0

# ---------------- UI ----------------
tk.Label(
    root, text="🎯 Smart Age Calculator",
    font=("Segoe UI", 22, "bold"),
    bg="#0f2027", fg="#00f2ff"
).pack(pady=15)

input_frame = tk.Frame(root, bg="#203a43")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Year", bg="#203a43", fg="white").grid(row=0, column=0)
tk.Label(input_frame, text="Month", bg="#203a43", fg="white").grid(row=0, column=1)
tk.Label(input_frame, text="Day", bg="#203a43", fg="white").grid(row=0, column=2)

year_entry = tk.Entry(input_frame, width=8)
month_entry = tk.Entry(input_frame, width=8)
day_entry = tk.Entry(input_frame, width=8)

year_entry.grid(row=1, column=0, padx=5)
month_entry.grid(row=1, column=1, padx=5)
day_entry.grid(row=1, column=2, padx=5)

tk.Button(
    root, text="Calculate Age",
    font=("Segoe UI", 12, "bold"),
    bg="#00f2ff", command=calculate_age
).pack(pady=10)

tk.Button(
    root, text="Reset",
    font=("Segoe UI", 10),
    bg="#ff6b6b", command=reset_app
).pack()

progress_label = tk.Label(
    root, text="📈 Year Progress",
    bg="#0f2027", fg="white"
)
progress_label.pack(pady=5)

progress_bar = ttk.Progressbar(
    root, length=300, mode="determinate"
)
progress_bar.pack(pady=5)

result_label = tk.Label(
    root, text="",
    font=("Segoe UI", 13),
    bg="#0f2027", justify="left"
)
result_label.pack()

# ---------------- QUIZ UI ----------------
quiz_frame = tk.Frame(root, bg="#2c5364")

tk.Label(
    quiz_frame, text="🧠 Age Based Quiz",
    font=("Segoe UI", 16, "bold"),
    bg="#2c5364", fg="white"
).pack(pady=10)

quiz_q = tk.Label(
    quiz_frame, text="",
    bg="#2c5364", fg="white"
)
quiz_q.pack(pady=5)

btn1 = tk.Button(quiz_frame, width=22)
btn2 = tk.Button(quiz_frame, width=22)
btn3 = tk.Button(quiz_frame, width=22)

btn1.pack(pady=3)
btn2.pack(pady=3)
btn3.pack(pady=3)

quiz_result = tk.Label(
    quiz_frame, text="",
    bg="#2c5364",
    font=("Segoe UI", 12)
)
quiz_result.pack(pady=8)

# ---------------- RUN ----------------
root.mainloop()
