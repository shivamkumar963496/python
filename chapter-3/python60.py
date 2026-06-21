# Q. Write a Python program to check whether withdrawal is allowed
# based on available balance.

# User se balance input lena
balance = float(input("Enter balance: "))

# User se withdrawal amount input lena
withdrawal = float(input("Enter withdrawal amount: "))

# Check karna ki withdrawal allowed hai ya nahi
if withdrawal <= balance:
    print("Withdrawal Allowed")

else:
    print("Withdrawal Not Allowed")