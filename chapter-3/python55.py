# Q. Write a Python program to check whether both numbers are positive,
# both negative, or mixed.

# User se first number input lena
a = int(input("Enter 1st number: "))

# User se second number input lena
b = int(input("Enter 2nd number: "))

# Check karna ki dono positive hain
if a > 0 and b > 0:
    print("Both Positive")

# Check karna ki dono negative hain
elif a < 0 and b < 0:
    print("Both Negative")

# Agar ek positive aur ek negative hai
else:
    print("Mixed")