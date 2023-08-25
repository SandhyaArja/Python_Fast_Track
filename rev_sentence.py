string="python"
rev=string[::-1] 
print(rev)



#second_method 

rev=""
for char in string:
    rev=char+rev 
print(rev)
