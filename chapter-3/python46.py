# Q. Write a Python program to print:
# "FizzBuzz" if number is divisible by both 3 and 5
# "Fizz" if number is divisible by 3
# "Buzz" if number is divisible by 5
# Otherwise print the number

# User se number input lena
num = int(input("Enter a number: "))

# Check karna ki number 3 aur 5 dono se divisible hai
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")

# Check karna ki number sirf 3 se divisible hai
elif num % 3 == 0:
    print("Fizz")

# Check karna ki number sirf 5 se divisible hai
elif num % 5 == 0:
    print("Buzz")

# Agar kisi se divisible nahi hai to number print karo
else:
    print(num)