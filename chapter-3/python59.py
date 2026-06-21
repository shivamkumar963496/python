# Q. Write a Python program to check whether a number is an Armstrong number.

# User se number input lena
n = int(input("Enter a number: "))

# Digits separate karna (3-digit number ke liye)
a = n // 100          # hundreds place
b = (n // 10) % 10    # tens place
c = n % 10            # ones place

# Armstrong sum calculate karna
armstrong_sum = a**3 + b**3 + c**3

# Check karna ki Armstrong number hai ya nahi
if armstrong_sum == n:
    print("Armstrong Number")
else:
    print("Not Armstrong")