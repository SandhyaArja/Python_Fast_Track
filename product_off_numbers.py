M=int(input())
N=int(input())
fac= 1 
for i in range(M,N+1):
    if i%2==1:
        fac*=i 
print(fac)
