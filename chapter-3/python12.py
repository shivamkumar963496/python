# Question 12:
# Take exam score from the user and print grade (A, B, C, D, or FAIL)

# Taking marks input
marks = int(input("ENTER EXAM SCORE = "))

# Checking grade
if marks >= 90:
    print("GRADE A")
elif marks >= 75:
    print("GRADE B")
elif marks >= 60:
    print("GRADE C")
elif marks >= 40:
    print("GRADE D")
else:
    print("FAIL")