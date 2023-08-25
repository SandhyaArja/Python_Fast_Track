try:  
    a = int(input())  
    b = int(input())  
    c = a/b
    print(c)  
except ZeroDivisionError:  
    print("Denominator can't be 0")  
except:  
    print("Unhandled Exception")




    #inputs 
    #a=19 
    #b=a 
    #will gives you unhandled exception
