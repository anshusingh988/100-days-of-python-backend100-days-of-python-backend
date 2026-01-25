# Student Grade System

name = input("Enter student name: ")

subjects = int(input("Enter number of subjects: "))
total_marks = 0

for i in range(subjects):
    marks = int(input(f"Enter marks for subject {i+1}: "))
    total_marks += marks

percentage = total_marks / subjects

# Grade Calculation
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"

print("\n--- Student Result ---")
print("Name:", name)
print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Grade:", grade)
