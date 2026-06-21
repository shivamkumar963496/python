a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a % b == 0 or b % a == 0:
    print("One is multiple of another")
else:
    print("Not multiple")