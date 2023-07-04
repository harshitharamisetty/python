mark=int(input("Enter the mark="))
if(mark>=90 and mark<=100):
    print("S grade")
elif(mark>=80 and mark<90):
    print("A grade")
elif(mark>=70 and mark<80):
    print("B grade")
elif(mark>=60 and mark<70):
    print("C grade")
elif(mark>=50 and mark<60):
    print("D grade")
elif(mark>=0 and mark<50):
    print("Fail")
else:
    print("Enter only Integer values")
