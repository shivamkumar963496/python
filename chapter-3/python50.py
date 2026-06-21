# Q. Write a Python program to display time of day based on hour:
# <12 → Morning
# 12–15 → Afternoon
# 16–19 → Evening
# >=20 → Night

# User se time (hour) input lena
time = int(input("Enter time (0-23): "))

# Time classification
if time < 12:
    print("Morning")

elif time < 16:
    print("Afternoon")

elif time < 20:
    print("Evening")

else:
    print("Night")