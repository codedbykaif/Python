marks = int(input("Enter your marks in subject1: "))

if marks > 100 or marks < 0:
    grade = "Invalid marks"
elif marks >= 90:
    grade = "ex"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)
