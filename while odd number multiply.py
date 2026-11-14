N=int(input("enter the number:"))
s,a=0,1
while a<=N:
    if a%2==1:
        s+=a
    a=a+1
print("odd number",s)
        
