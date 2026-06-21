# Q. Write a Python program to calculate discount based on customer type.
# Premium customer → 20% discount
# Regular customer → 10% discount

# User se product price input lena
price = float(input("Enter product price: "))

# User se customer type input lena
ctype = input("Enter customer type (regular/premium): ").lower()

# Discount calculation
if ctype == "premium":
    discount = price * 0.20
else:
    discount = price * 0.10

# Discount display karna
print("Discount =", discount)