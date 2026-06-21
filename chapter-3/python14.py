# Question 14:
# Take username from the user and provide access type (Admin, Guest, or Invalid)

# Taking username input
username = input("ENTER USERNAME: ")

# Converting username to lowercase
username = username.lower()

# Checking access type
if username == "admin":
    print("ADMIN ACCESS")
elif username == "guest":
    print("GUEST ACCESS")
else:
    print("INVALID USER")