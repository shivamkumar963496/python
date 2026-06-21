# Question 8:
# Take two numbers from the user and print which one is greatest or if both are equal

# Taking input
a = int(input("ENTER 1ST NUMBER = "))
b = int(input("ENTER 2ND NUMBER = "))

# Checking greatest number
if a > b:
    print("A IS GREATEST")
elif b > a:
    print("B IS GREATEST")
else:
    print("BOTH ARE EQUAL")