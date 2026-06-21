# Question 4:
# Take marks from the user and print grade (FAIL, PASS, FIRST CLASS, DISTINCTION)

# Taking marks input
marks = int(input("ENTER MARKS = "))

# Checking grade
if marks < 35:
    print("FAIL")
elif marks <= 59:
    print("PASS")
elif marks <= 79:
    print("FIRST CLASS")
else:
    print("DISTINCTION")