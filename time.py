n=float(input("Enter the seconds:"))
print("houre=",n//3600)
n=n%3600
print("minutes=",n//60)
n=n%60
print("seconds=",n)
print("millisec",n*0.100)
