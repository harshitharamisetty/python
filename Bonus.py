salary=float(input("Enter the salary= "))
if salary==10000:
    print(0.05*salary,"bonus")
elif salary>10000:
    print(0.075*salary,"bonus")
elif salary<=2000:
    experience=int(input("Enter the year="))
if experience>5:
    print(0.2*salary,"bonus")
elif experience<5:
    print(0.1*salary,"bonus")
else:
    print("invalid input")
    
