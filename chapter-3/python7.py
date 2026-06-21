# Question 7:
# Take a number from the user and check whether it is divisible by 3, 5, or both

# Taking number input
num = int(input("ENTER A NUMBER = "))

# Checking divisibility
if num % 3 == 0 and num % 5 == 0:
    print("DIVISIBLE BY BOTH 3 AND 5")
elif num % 3 == 0:
    print("DIVISIBLE BY 3")
elif num % 5 == 0:
    print("DIVISIBLE BY 5")
else:
    print("NOT DIVISIBLE BY 3 OR 5")