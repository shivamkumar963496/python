# Q. Write a Python program to check special ticket discount eligibility.
# Discount is available if:
# Age is <= 12 OR Age is >= 60 OR Gender is Female

# User se age input lena
age = int(input("Enter your age: "))

# User se gender input lena
gender = input("Enter your gender (M/F): ").lower()

# Discount condition check karna
if age <= 12 or age >= 60 or gender == "f":
    print("Special Discount Available")

else:
    print("No Discount Available")