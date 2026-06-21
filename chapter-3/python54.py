# Q. Write a Python program to check promotion eligibility.
# Promotion is given if salary > 50000 and experience >= 5 years.

# User se salary input lena
salary = int(input("Enter your salary: "))

# User se experience input lena
experience = int(input("Enter your experience (in years): "))

# Promotion eligibility condition check karna
if salary > 50000 and experience >= 5:
    print("Promotion Eligible")

else:
    print("Not Eligible")