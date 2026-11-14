L=[1,2,3,4,5,6,7,8,9,10]
M=list(map(lambda x: x%2==0,L))
N=list(filter(lambda x: x%2!=0,L))
print(M)
print(N)
