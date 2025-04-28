a=int(input("Enter units: "))
if(a<100):
    bill=a*5
    print("The total bill is:",bill)
if(a>=100 and a<200):
    bill=(a-100)*7
    firsthundred=100*5
    bill=firsthundred+bill
    print("The total bill is:",bill)
if(a>=200):
    firsthundred=100*5
    a=a-100
    nexthundred=100*7
    a=a-100
    bill=firsthundred+nexthundred+(a*10)
    print("The total bill is:",bill)