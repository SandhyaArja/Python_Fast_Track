def count_of_lowercase_and_uppercase_letters(word):
    count_of_lowercase=0
    count_of_uppercase=0
    for i in word:
        
        if i.upper()==i:
            count_of_uppercase += 1
            
        else:
            count_of_lowercase += 1
    
    print(count_of_uppercase)
    print(count_of_lowercase)
    
word= input()
count_of_lowercase_and_uppercase_letters(word)

