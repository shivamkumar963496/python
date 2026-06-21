# Q. Write a Python program to check whether both numbers are even,
# both odd, or mixed.

# User se first number input lena
a = int(input("Enter first number: "))

# User se second number input lena
b = int(input("Enter second number: "))

# Check karna ki dono even hain
if a % 2 == 0 and b % 2 == 0:
    print("Both Even")

# Check karna ki dono odd hain
elif a % 2 != 0 and b % 2 != 0:
    print("Both Odd")

# Agar ek even aur ek odd hai
else:
    print("Mixed")