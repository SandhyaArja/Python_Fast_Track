#Recursion
#A function calling itself is called a Recursion



def factorial(n):  # Recursive Function
   if n == 1:  # Base Case
       return 1
   return n * factorial(n - 1)  # Recursion
num = int(input())
result = factorial(num)
print(result)




#A recursive function terminates when base condition is met
