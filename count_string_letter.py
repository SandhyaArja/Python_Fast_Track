s=input()
all_freq={} 
for i in s:
    if i in all_freq:
        all_freq[i]+=1 
    else:
        all_freq[i]=1 
print(str(all_freq))
