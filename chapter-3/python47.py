# Q. Write a Python program to classify performance based on score:
# >=90 → Excellent
# >=70 → Good
# >=50 → Average
# <50 → Poor

# User se score input lena
score = float(input("Enter your score: "))

# Performance classification
if score >= 90:
    print("Excellent")

elif score >= 70:
    print("Good")

elif score >= 50:
    print("Average")

else:
    print("Poor")