# Q. Write a Python program to classify a number as:
# Less than 0, Exactly 100, Between 0 and 100, or Greater than 100.

# User se number input lena
n = int(input("Enter number: "))

# Check karna ki number 0 se chhota hai
if n < 0:
    print("Less than 0")

# Check karna ki number exactly 100 hai
elif n == 100:
    print("Exactly 100")

# Check karna ki number 0 aur 100 ke beech hai
elif 0 <= n < 100:
    print("Between 0 and 100")

# Agar number 100 se bada hai
else:
    print("Greater than 100")