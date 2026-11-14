N=int(input("enter N num:"))
s=0
for w in range(1,N+1):
    for i in range(2,w):
        if(w%i==0):
           break
    else:
        s+=w
print("sum of all prime numbers from 1 to N:",s)

