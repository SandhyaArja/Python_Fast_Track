
string=input().split()
rev_word=[]
N=len(string)
for i in range(N):
    rev_word.append(string[N-i-1])
out=" ".join(rev_word)
print(out)
