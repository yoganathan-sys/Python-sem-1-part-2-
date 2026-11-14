N=input("any string:")
i,v=0,0
while i<len(N):
    if N[i] in "aeiouAEIOU":
        v=v+1
    i=i+1
print("no of vowels:",v)
