import re
 
string = "The quick brown fox jumps over the lazy dog"
pattern = "[a-m]" #will retrieve only between a-m
result = re.findall(pattern, string)
 
print(result)

import re 
string ="the quick brown for jumps over the lazy dog"
pattern='[^a-m]' #will retrieve every thing except a-m
result=re.findall(pattern,string)
print(result)
