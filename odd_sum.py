

n=int(input())
odd_sum= 0
for num in range(1,n+1):
    if num%2==0:
        continue 
    odd_sum+=num 
print(odd_sum)
