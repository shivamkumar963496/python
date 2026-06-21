num = int(input("Enter number: "))

# outside range
if not(num > 10 and num < 20):
    print("Not between 10 and 20")
else:
    print("Between 10 and 20")