# Q. Write a Python program to classify a number into ranges:
# 0–50, 51–100, 101–200, Above 200

# User se number input lena
num = int(input("Enter a number: "))

# Range check karna
if num <= 50:
    print("0-50")

elif num <= 100:
    print("51-100")

elif num <= 200:
    print("101-200")

else:
    print("Above 200")