N=int(input())
for num in range(1,N+1):
    if num%3==0 or num%5==0:
        continue 
    print(num)
