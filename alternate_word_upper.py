s=input()
l=len(s)
word=""
for i in range(l):
    if i%2==0:
        word+=s[i].upper()
    else:
        word+=s[i].lower()
print(word)
