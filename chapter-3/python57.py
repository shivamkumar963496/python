# Q. Write a Python program to check whether a character is:
# Uppercase, Lowercase, Digit, or Special Character.

# User se character input lena
ch = input("Enter a character: ")

# Check karna ki character uppercase hai
if ch.isupper():
    print("Uppercase")

# Check karna ki character lowercase hai
elif ch.islower():
    print("Lowercase")

# Check karna ki character digit hai
elif ch.isdigit():
    print("Digit")

# Agar koi special character hai
else:
    print("Special Character")