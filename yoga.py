N=int(input("Enter the cost:"))
if N>=1001 and N<=2000:
    print("discount:",N*5/100)
    print("actual amount:",N)
    print("total amount:",N-N*5/100)
elif N>=2001 and N<=4000:
    print("discount:",N*10/100)
    print("actual amt:",N)
    print("total amt:",N-N*10/100)
elif N>=4001 and N<=8000:
    print("discount:",N*20/100)
    print("actual amt:",N)
    print("total amt:",N-N*20/100)
elif N>8000:
    print("discount:",N*25/100)
    print("actual amt:",N)
    print("total amt:",N-N*25/100)
else:
    print("discount=0")
    print("actual amount:",N)
    print("total amt:",N)
    
