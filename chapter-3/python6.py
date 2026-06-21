# Question 6:
# Take salary from the user and classify as LOW, MEDIUM, or HIGH SALARY

# Taking salary input
salary = int(input("ENTER YOUR SALARY = "))

# Checking salary category
if salary < 30000:
    print("LOW SALARY")
elif salary <= 70000:
    print("MEDIUM SALARY")
else:
    print("HIGH SALARY")