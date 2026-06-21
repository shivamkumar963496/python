# Q. Write a Python program to check the type of triangle:
# Equilateral, Isosceles, or Scalene based on three sides.

# User se triangle ki sides input lena
a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

# Check karna ki triangle valid hai ya nahi (important improvement)
if a + b <= c or a + c <= b or b + c <= a:
    print("Invalid Triangle")

# Check karna ki teeno sides equal hain
elif a == b == c:
    print("Equilateral Triangle")

# Check karna ki koi do sides equal hain
elif a == b or b == c or c == a:
    print("Isosceles Triangle")

# Agar sab sides different hain
else:
    print("Scalene Triangle")