# Question 11:
# Take a number from the user and check whether it is 1-digit, 2-digit, or 3-digit

# Taking number input
num = int(input("ENTER A NUMBER = "))

# Checking digit count
if 0 <= num <= 9:
    print("1 DIGIT NUMBER")
elif 10 <= num <= 99:
    print("2 DIGIT NUMBER")
elif 100 <= num <= 999:
    print("3 DIGIT NUMBER")
else:
    print("MORE THAN 3 DIGITS")