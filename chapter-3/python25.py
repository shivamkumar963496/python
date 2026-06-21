salary=float(input("ENTER YOUR SALARY = "))
exprience=int(input("ENTER YOUR EXPERIENCE = "))

if exprience<=2:
    bonus=salary*0.05
    
elif exprience<=5:
    bonus=salary*0.10
    
else:
    bonus=salary*0.15
    
print("Bonus:", bonus)