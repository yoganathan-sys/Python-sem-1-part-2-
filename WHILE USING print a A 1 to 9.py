n=input("enter any string:")
i,v,b,c,d,q=0,0,0,0,0,0
while i<len(n):
    a=n[i]
    if 'A'<=a and a<='Z':
        v=v+1
    elif 'a'<=a and a<='z':
        b=b+1
    elif a==" ":
        c=c+1
    elif '0'<=a and a<='9':
        d=d+1
    else:
        q=q+1
    i=i+1
print("-------CHARATER ANALYSIS--------")
print("caps",v)
print("small",b)
print("space",c)
print("numbers",d)
print("symbol",q)
print("total=",v+b+c+d+q)

        

