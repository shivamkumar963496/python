income=int(input("ENTER YOUR INCOME = "))

if income<250000:
    print("NO TAX")
elif income<=500000:
    print("tax = ",income*0.05)
    
elif income<=1000000:
    print("tax = ",income*0.10)
    
else:
    print("tax = ",income*0.20)