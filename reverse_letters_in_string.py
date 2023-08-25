string=input().split()
rev_words=[]
for i in string:
    rev_words.append(i[::-1])
    
out=" ".join(rev_words)
print(out)
