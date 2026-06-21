# Q. Write a Python program to determine insurance premium category based on age:
# Age < 25 → High Premium
# Age 25–50 → Normal Premium
# Age > 50 → Low Premium

# User se age input lena
age = int(input("Enter age: "))

# Premium category check karna
if age < 25:
    print("High Premium")

elif age <= 50:
    print("Normal Premium")

else:
    print("Low Premium")