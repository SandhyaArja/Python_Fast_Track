def fizz_buzz(number):
    if ((number%3==0)and(number%5==0)):
        strn="FizzBuzz"
    elif ((number%3==0)):
        strn="Fizz"
    elif (number%5==0):
        strn="Buzz"
    else:
        strn=number 
    return strn
number=int(input())
result=fizz_buzz(number)
print(result)
