# Question 10:
# Take a year from the user and check whether it is a Leap Year or not

# Taking year input
year = int(input("ENTER A YEAR = "))

# Checking leap year condition
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("LEAP YEAR")
else:
    print("NOT A LEAP YEAR")