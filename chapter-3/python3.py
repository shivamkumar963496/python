# Question 3:
# Take age from the user and classify as Child, Teen, or Adult

# Taking age input
age = int(input("ENTER AGE = "))

# Checking age category
if age < 13:
    print("CHILD")
elif age <= 19:
    print("TEEN")
else:
    print("ADULT")