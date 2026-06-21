# Question 5:
# Take temperature from the user and classify as COLD, WARM, or HOT

# Taking temperature input
temp = int(input("ENTER TEMPERATURE = "))

# Checking temperature condition
if temp < 15:
    print("COLD")
elif temp <= 30:
    print("WARM")
else:
    print("HOT")